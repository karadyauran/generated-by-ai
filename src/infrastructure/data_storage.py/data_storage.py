import json
from typing import List
from src.domain.models.transaction import Transaction

class DataStorage:
    """
    Handles storing and retrieving transaction data from a JSON file.
    """

    def __init__(self, filename: str):
        """
        Initialize the DataStorage with a filename.

        :param filename: The name of the file where transactions are stored.
        """
        self.filename = filename

    def save_transactions(self, transactions: List[Transaction]):
        """
        Save a list of transactions to the JSON file.

        :param transactions: A list of Transaction objects to be stored.
        """
        data = [transaction.to_dict() for transaction in transactions]
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_transactions(self) -> List[Transaction]:
        """
        Load transactions from the JSON file and return as a list of Transaction objects.

        :return: A list of Transaction objects.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Transaction.from_dict(item) for item in data]
        except FileNotFoundError:
            # Return an empty list if the file does not exist
            return []

    def add_transaction(self, transaction: Transaction):
        """
        Add a single transaction to the existing data in the JSON file.

        :param transaction: A Transaction object to add.
        """
        transactions = self.load_transactions()
        transactions.append(transaction)
        self.save_transactions(transactions)