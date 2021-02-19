"""
    CalculationMethods.py

    Calculates the current of a circuit
    using Kirchhoff's voltage law

    Dario Marroquin 18269 (dariomarroquin)
    Pablo Ruiz 18259 (PingMaster99)

    Version 1.0
    Updated February 19, 2020
"""
from sympy import *

# Needed symbols
x = symbols('x')


def fixed_point(function, x0, expected_error, imax):
    """
    Calculates the root estimate using the fixed point method
    :param function: function to be evaluated
    :param x0: initial point
    :param expected_error: expected error in percent
    :param imax: maximum number of iterations
    :return: root, iteration numbers, and error
    """
    xr = x0
    iteration = 0
    current_error = float('inf')

    while current_error >= expected_error and iteration < imax:
        xr_old = xr
        xr = parse_expr(function).evalf(subs={x: xr_old})
        iteration += 1

        if xr != 0:
            current_error = abs((xr - xr_old) / xr) * 100
    if current_error < expected_error and xr.is_real:
        # DC current only uses real values
        return xr, iteration, current_error
    else:
        return None


def calculate_circuit(voltage, resistance, power, error, initial_point):
    """
    Calculates the current of a circuit with a lightbulb or a LED
    :param voltage: voltage source
    :param resistance: resistor value
    :param power: power consumed by the bulb (use 0 for a led)
    :param error: expected error
    :param initial_point: initial point of estimation
    :return: current flowing through the circuit
    """

    # A voltage of 0 means the circuit has no current
    if voltage == 0:
        return 0

    # If the bulb consumes power, we check for which solution is optimal
    if power != 0:
        kirchhoff = f"({resistance} * x ** 2 + {power}) / {voltage}"
        first_result = fixed_point(kirchhoff, initial_point, error, 100)

        kirchhoff1 = f"(({voltage} * x - {power})/{resistance}) ** 0.5"
        second_result = fixed_point(kirchhoff1, initial_point, error, 100)

        if first_result is not None and second_result is not None:
            first_current = first_result[0]
            second_current = second_result[0]

            # Lamp resistance based upon the assumption that the voltage source is close to its requirements
            # Note that instead of a lamp it could be any electronic component that consumes power
            lamp_resistance = voltage ** 2 / power

            # We calculate the lamp resistance based on the obtained currents
            first_lamp_resistance = (voltage - resistance * first_current) / first_current
            second_lamp_resistance = (voltage - resistance * second_current) / second_current

            first_current_distance = abs(lamp_resistance - first_lamp_resistance)
            second_current_distance = abs(lamp_resistance - second_lamp_resistance)

            # The current which results in a resistance value for the lamp that is closer to reality is returned
            if first_current_distance < second_current_distance:
                return first_current
            else:
                return second_current

        elif first_result is not None:
            first_result = first_result[0]
            return first_result
        elif second_result is not None:
            second_result = second_result[0]
            return second_result
        else:
            return None

    # When the power is 0, a simpler equation can be used
    elif resistance != 0:
        kirchhoff = f"{voltage} / {resistance}"
        result = fixed_point(kirchhoff, initial_point, error, 100)
        if result is not None:
            return result[0]

    return None
