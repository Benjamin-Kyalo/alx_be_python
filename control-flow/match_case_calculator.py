# match_case_calculator.py

# 1. Read inputs as floats
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Ask for the operation
operation = input("Choose the operation (+, -, *, /): ").strip()

# 3. Use match-case to decide
match operation:
    case "+":
        result = num1 + num2

    case "-":
        result = num1 - num2

    case "*":
        result = num1 * num2

    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            # Stop further execution
            exit()
        result = num1 / num2

    case _:
        print("Unknown operation.")
        exit()

# 4. Print the result
print(f"The result is {result}.")
