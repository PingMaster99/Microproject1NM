from sympy import *

# Needed symbols
x = symbols('x')


def newton_raphson(function, x0, expected_error, imax):
    """
    Calculates the root estimate using the Newton-Raphson method
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
        xr = xr_old - ((parse_expr(function).evalf(subs={x: xr_old})) /
                       (diff(parse_expr(function)).evalf(subs={x: xr_old})))
        iteration += 1

        if xr != 0:
            current_error = abs((xr - xr_old) / xr) * 100

    return xr, iteration, current_error


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


def calculate_circuit(voltage, resistance, power, error):

    kirchhoff = f"{resistance} * x ** 2 - {voltage} * x + {power}"
    result = fixed_point(kirchhoff, 0, error, 100)
    if result is not None:
        return result[0]

    return None
