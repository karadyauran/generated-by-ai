from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class Budget:
    """
    A class to represent budgeting data.
    """
    category: str
    limit: float = 0.0
    spent: float = 0.0

    def update_spent(self, amount: float):
        """
        Update the total spent in the category.
        :param amount: Amount to add to the spent.
        """
        self.spent += amount

    def reset_spent(self):
        """
        Reset the spent amount to zero.
        """
        self.spent = 0.0

    def is_within_budget(self) -> bool:
        """
        Check if the current spent amount is within the budget limit.
        :return: True if within budget, False otherwise.
        """
        return self.spent <= self.limit


class BudgetManager:
    """
    A class to manage multiple budget categories.
    """
    def __init__(self):
        self.budgets: Dict[str, Budget] = {}

    def add_budget(self, category: str, limit: float):
        """
        Add or update a budget for a specific category.
        :param category: The name of the category.
        :param limit: The spending limit.
        """
        self.budgets[category] = Budget(category=category, limit=limit)

    def get_budget(self, category: str) -> Optional[Budget]:
        """
        Retrieve a budget for a specific category.
        :param category: The name of the category.
        :return: The Budget instance or None if not found.
        """
        return self.budgets.get(category)

    def update_category_spent(self, category: str, amount: float):
        """
        Update the spent amount for a specific category.
        :param category: The name of the category.
        :param amount: The amount to add to the spent.
        """
        if category in self.budgets:
            self.budgets[category].update_spent(amount)

    def check_budget_exceeded(self, category: str) -> bool:
        """
        Check if the budget for a specific category is exceeded.
        :param category: The name of the category.
        :return: True if exceeded, otherwise False.
        """
        budget = self.get_budget(category)
        return not budget.is_within_budget() if budget else False