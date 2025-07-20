# pattern_drawing.py

# 1. Prompt the user and convert to integer
size = int(input("Enter the size of the pattern: "))

# 2. Initialize row counter
row = 1

# 3. Outer loop: repeat for each row
while row <= size:
    # 4. Inner loop: print one row of asterisks
    for col in range(1, size + 1):
        print("*", end="")  # stay on the same line

    # 5. Move to the next line after finishing the row
    print()

    # 6. Advance to the next row
    row += 1
