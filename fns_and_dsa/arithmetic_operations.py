# arithmetic_operations.py
# This module defines a function to perform basic arithmetic operations.

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    - operation: A string specifying which operation to perform:
      'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    - The result of the arithmetic operation (float),
      or an error message (str) for unsupported operations or division by zero.
    """
    if operation == 'add':
        # Addition: return the sum of num1 + num2
        return num1 + num2

    elif operation == 'subtract':
        # Subtraction: return the difference (num1 - num2)
        return num1 - num2

    elif operation == 'multiply':
        # Multiplication: return the product of num1 * num2
        return num1 * num2

    elif operation == 'divide':
        # Division: check for division by zero first
        if num2 == 0:
            # Return an explicit error message for zero division
            return "Error: Division by zero"
        # Safe to perform division
        return num1 / num2

    else:
        # Unsupported operation string
        return f"Error: Unsupported operation '{operation}'"
