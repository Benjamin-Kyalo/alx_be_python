import sys
from bank_account import BankAccount


def main():
    # Initialize account with default or example starting balance
    account = BankAccount(100.0)

    # Check for at least one argument
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and optional amount
    command, *params = sys.argv[1].split(':')
    amount = None
    if params:
        try:
            amount = float(params[0])
        except ValueError:
            print("Error: amount must be a number.")
            sys.exit(1)

    # Execute the requested operation
    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")
            print("Usage examples:")
            print("  python main-0.py deposit:50")
            print("  python main-0.py withdraw:20")
            print("  python main-0.py display")
            sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
