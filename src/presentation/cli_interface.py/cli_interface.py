from src.infrastructure.data_storage import DataStorage
from src.infrastructure.authentication import Authentication
from src.domain.models.transaction import Transaction
from src.domain.services.budget_manager import BudgetManager

class CLIInterface:
    """
    Command-line interface for interacting with the Personal Finance Tracker application.
    """

    def __init__(self, transaction_file: str, auth_file: str):
        """
        Initialize the CLIInterface with data and authentication handlers.

        :param transaction_file: Path to the transaction data file.
        :param auth_file: Path to the authentication data file.
        """
        self.data_storage = DataStorage(transaction_file)
        self.authentication = Authentication(auth_file)
        self.budget_manager = BudgetManager()

    def login(self, username: str, password: str) -> bool:
        """
        Authenticate a user.

        :param username: The user's username.
        :param password: The user's password.
        :return: True if logged in successfully, else False.
        """
        return self.authentication.authenticate_user(username, password)

    def register(self, username: str, password: str):
        """
        Register a new user.

        :param username: The new user's username.
        :param password: The new user's password.
        """
        self.authentication.register_user(username, password)

    def add_transaction(self, amount: float, date: str, category: str, description: str = ""):
        """
        Add a new financial transaction.

        :param amount: Transaction amount.
        :param date: Date of the transaction.
        :param category: Category of the transaction.
        :param description: Optional description of the transaction.
        """
        transaction = Transaction(amount, date, category, description)
        self.data_storage.add_transaction(transaction)

    def set_budget(self, category: str, amount: float):
        """
        Set a financial budget for a category.

        :param category: The category name.
        :param amount: The budget amount to set.
        """
        self.budget_manager.set_budget(category, amount)

    def display_budgets(self) -> str:
        """
        Retrieve and return a string representation of all budgets.

        :return: String representation of budgets.
        """
        return str(self.budget_manager)
