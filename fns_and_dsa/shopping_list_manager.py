# shopping_list_manager.py
# A simple shopping list manager using Python lists for dynamic data storage.

def display_menu():
    """
    Display the main menu options to the user.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """
    Main function that runs the shopping list manager loop.
    Initializes an empty shopping list and handles user input.
    """
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()  # Show options
        try:
            # Prompt for a numeric choice between 1 and 4
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")

        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"Item '{item}' not found in the shopping list.")

        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Current shopping list:")
                for index, entry in enumerate(shopping_list, start=1):
                    print(f"{index}. {entry}")
            else:
                print("The shopping list is currently empty.")

        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle out-of-range numeric choices
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()  # Run the program when executed directly
