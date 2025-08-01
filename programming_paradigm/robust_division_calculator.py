def safe_divide(numerator, denominator):
    """
    Safely divide two values, handling errors for non-numeric inputs and division by zero.

    :param numerator: value to be used as numerator (string or numeric)
    :param denominator: value to be used as denominator (string or numeric)
    :return: result string or error message
    """
    try:
        # Attempt conversion to float
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
