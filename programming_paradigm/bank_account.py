class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        """
        Initialize a new BankAccount instance.
        :param initial_balance: starting balance for the account (defaults to 0.0)
        """
        self._balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Add funds to the account.
        :param amount: positive amount to deposit
        :raises ValueError: if amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw funds from the account if sufficient balance exists.
        :param amount: positive amount to withdraw
        :return: True if successful, False if insufficient funds
        :raises ValueError: if amount is not positive
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            return False
        self._balance -= amount
        return True

    def display_balance(self) -> None:
        """
        Print the current balance to two decimal places.
        """
        print(f"Current Balance: ${self._balance:.2f}")
