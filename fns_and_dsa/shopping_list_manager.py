# A shopping list manager for dynamic storage

def display_menu():
    # Show the main options to the user
    print("\nShopping List Manager")
    print("1. Add item to list")
    print("2. Remove item from list")
    print("3. Display list")
    print("4. Exit")

def main():
    # Start with an empty list
    shopping_list = []

    # Keep running until the user chooses to exit
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Option 1: Add a new item
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"✅ Item '{item}' added to the list.")

        elif choice == '2':
            # Option 2: Remove an existing item
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑 Removed '{item}' from the list.")
            else:
                # Item wasn't found in the list
                print(f"⚠️ Item '{item}' not found in your shopping list.")

        elif choice == '3':
            # Option 3: Show all items
            if shopping_list:
                print("\n🛒 Your current shopping list:")
                for index, entry in enumerate(shopping_list, start=1):
                    print(f"  {index}. {entry}")
            else:
                # List is empty
                print("\nℹ️ Your shopping list is empty.")

        elif choice == '4':
            # Option 4: Exit the program
            print("👋 Exiting the shopping list manager. Goodbye!")
            break

        else:
            # User entered something other than 1–4
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

# Only run main() when this script is executed directly (not imported)
if __name__ == "__main__":
    main()
