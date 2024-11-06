from typing import Any, Dict

class Transaction:
    """
    Represents a financial transaction.
    """
    def __init__(self, transaction_id: int, user_id: int, trans_type: str, category: str, amount: float, date: str):
        """
        Initialize a transaction.
        :param transaction_id: Unique identifier for the transaction
        :param user_id: ID of the user to whom the transaction belongs
        :param trans_type: Type of the transaction ('income' or 'expense')
        :param category: Category of the transaction
        :param amount: Amount involved in the transaction
        :param date: Date of the transaction
        """
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.trans_type = trans_type
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Transaction instance to a dictionary.
        :returns: Dictionary representation of the transaction
        """
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'type': self.trans_type,
            'category': self.category,
            'amount': self.amount,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Transaction':
        """
        Create a Transaction instance from a dictionary.
        :param data: Dictionary with transaction data
        :returns: Transaction instance
        """
        return cls(
            transaction_id=data.get('transaction_id', 0),
            user_id=data['user_id'],
            trans_type=data['type'],
            category=data['category'],
            amount=data['amount'],
            date=data['date']
        )

    def __repr__(self) -> str:
        """
        Return the string representation of the transaction.
        :returns: String representation
        """
        return (f"Transaction(id={self.transaction_id}, user_id={self.user_id}, type={self.trans_type}, "
                f"category={self.category}, amount={self.amount}, date={self.date})")
