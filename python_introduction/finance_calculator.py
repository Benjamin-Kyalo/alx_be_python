# Task Description:

# You will create a script named finance_calculator.py. 
# This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
savings = income - expenses

annual_without_interest = savings * 12
annual_with_interest = annual_without_interest * 1.05

print(f"Your monthly savings are ${savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_with_interest:.2f}.")
