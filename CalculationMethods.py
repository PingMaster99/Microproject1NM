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
    if current_error < expected_error:
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
    if voltage == 0:
        return 0

    if power != 0:
        kirchhoff = f"({resistance} * x ** 2 + {power}) / {voltage}"
        kirchhoff1 = f"(({voltage} * x - {power})/{resistance}) ** 0.5"

        first_result = fixed_point(kirchhoff, initial_point, error, 100)
        second_result = fixed_point(kirchhoff1, initial_point, error, 100)

        if first_result is not None and second_result is not None:
            first_current = first_result[0]
            second_current = second_result[0]

            lamp_resistance = voltage ** 2 / power

            first_lamp_resistance = (voltage - resistance * first_current) / first_current
            second_lamp_resistance = (voltage - resistance * second_current) / second_current

            first_current_distance = abs(lamp_resistance - first_lamp_resistance)
            second_current_distance = abs(lamp_resistance - second_lamp_resistance)

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

    elif resistance != 0:
        kirchhoff = f"{voltage} / {resistance}"
        result = fixed_point(kirchhoff, initial_point, error, 100)
        if result is not None:
            return result[0]

    return None
