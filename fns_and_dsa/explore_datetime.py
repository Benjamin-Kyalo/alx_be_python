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

