# explore_datetime.py
# Demonstrates basic usage of the datetime module: displaying current datetime and calculating a future date.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtain and print the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    # Save current date and time
    current_date = datetime.now()
    # Format as string
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")


def calculate_future_date(days_to_add: int):
    """
    Calculate and print the date after adding a specified number of days to today.

    Parameters:
    - days_to_add: number of days to add (integer)
    """
    # Save current date and time
    today = datetime.now()
    # Compute future date by adding a timedelta
    future_date = today + timedelta(days=days_to_add)
    # Format result as YYYY-MM-DD
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    """
    Execute both display_current_datetime and calculate_future_date with user input.
    """
    display_current_datetime()
    # Prompt user for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
        return

    calculate_future_date(days)


if __name__ == "__main__":
    main()


# temp_conversion_tool.py
# Illustrates variable scope and conversion functions between Celsius and Fahrenheit.

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius using the global factor.

    Parameters:
    - fahrenheit: temperature in degrees Fahrenheit

    Returns:
    - Equivalent temperature in degrees Celsius
    """
    # Use the global conversion factor
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit using the global factor.

    Parameters:
    - celsius: temperature in degrees Celsius

    Returns:
    - Equivalent temperature in degrees Fahrenheit
    """
    # Use the global conversion factor
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """
    Prompt the user for a temperature and its unit, then perform conversion.
    """
    # Prompt for numeric temperature value
    try:
        temp_str = input("Enter the temperature to convert: ")
        temp_value = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit and normalize
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        # Convert from Fahrenheit to Celsius
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result}°C")
    elif unit == 'C':
        # Convert from Celsius to Fahrenheit
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result}°F")
    else:
        # Invalid unit specified
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")


if __name__ == "__main__":
    main()
