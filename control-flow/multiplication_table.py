# multiplication_table.py

# 1. Prompt the user and convert to integer
number = int(input("Enter a number to see its multiplication table: "))

# 2. Loop from 1 through 10
for i in range(1, 11):
    product = number * i
    # 3. Print each line in the format "X * Y = Z"
    print(f"{number} * {i} = {product}")
