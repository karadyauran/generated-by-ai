from datetime import datetime
from dataclasses import dataclass

@dataclass
class Transaction:
    """
    A class to represent a financial transaction.
    """
    id: int
    date: str
    amount: float
    category: str
    description: str = ""
    
    def __post_init__(self):
        """
        Initialize the transaction date ensuring it's properly formatted.
        """
        if isinstance(self.date, datetime):  # Ensure the date is in the desired format
            self.date = self.date.strftime('%Y-%m-%d')

    def to_dict(self):
        """
        Convert the transaction to a dictionary representation.
        :return: A dictionary representation of the transaction.
        """
        return {
            'id': self.id,
            'date': self.date,
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Transaction instance from a dictionary.
        :param data: Dictionary containing data.
        :return: Transaction instance.
        """
        return Transaction(
            id=data.get('id', 0),
            date=data.get('date', datetime.now().strftime('%Y-%m-%d')),
            amount=data.get('amount', 0.0),
            category=data.get('category', ""),
            description=data.get('description', "")
        )

    def is_valid(self):
        """
        Validate the transaction data.
        :return: Boolean indicating if the transaction is valid.
        """
        if not self.id or self.amount <= 0 or not self.category:
            return False
        return True