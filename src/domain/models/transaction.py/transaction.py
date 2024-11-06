class Transaction:
    """
    Class representing a financial transaction.
    """

    def __init__(self, amount: float, date: str, category: str, description: str = ""):
        """
        Initialize a Transaction instance.

        :param amount: Amount of the transaction, positive for income, negative for expenses.
        :param date: Date of the transaction in "YYYY-MM-DD" format.
        :param category: Category of the transaction, e.g., 'Groceries', 'Salary'.
        :param description: Optional description of the transaction.
        """
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def to_dict(self) -> dict:
        """
        Convert the transaction to a dictionary format.

        :return: A dictionary representation of the transaction.
        """
        return {
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "description": self.description
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Create a Transaction instance from a dictionary.

        :param data: A dictionary with transaction data.
        :return: An instance of Transaction.
        """
        return Transaction(
            amount=data.get("amount", 0.0),
            date=data.get("date", ""),
            category=data.get("category", ""),
            description=data.get("description", "")
        )

    def __str__(self) -> str:
        """
        Return a string representation of the transaction.

        :return: A string that represents the transaction.
        """
        return f"Transaction(amount={self.amount}, date='{self.date}', category='{self.category}', description='{self.description}')"

    def __eq__(self, other) -> bool:
        """
        Compare two transactions to see if they are equal.

        :param other: Another Transaction instance to compare.
        :return: True if the transactions are equivalent, False otherwise.
        """
        return (
            isinstance(other, Transaction) and
            self.amount == other.amount and
            self.date == other.date and
            self.category == other.category and
            self.description == other.description
        )
