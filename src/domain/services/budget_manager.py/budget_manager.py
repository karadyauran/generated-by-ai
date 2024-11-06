class BudgetManager:
    """
    A class to manage budgets for different categories.
    """

    def __init__(self):
        """
        Initializes the BudgetManager with an empty budget mapping.
        """
        self.budgets = {}

    def set_budget(self, category: str, amount: float):
        """
        Set a budget for a specific category.

        :param category: The category for which to set the budget.
        :param amount: The budget amount.
        """
        if amount < 0:
            raise ValueError("Budget amount cannot be negative.")
        self.budgets[category] = amount

    def get_budget(self, category: str) -> float:
        """
        Get the budget for a specific category.

        :param category: The category for which to get the budget.
        :return: The budget amount for the category, or 0 if not set.
        """
        return self.budgets.get(category, 0.0)

    def remove_budget(self, category: str):
        """
        Remove the budget for a specific category.

        :param category: The category for which to remove the budget.
        """
        if category in self.budgets:
            del self.budgets[category]

    def calculate_remaining_budget(self, category: str, expenses: float) -> float:
        """
        Calculate the remaining budget for a category after expenses.

        :param category: The category to evaluate.
        :param expenses: Total expenses for the category.
        :return: Remaining budget amount, or negative if over budget.
        """
        if expenses < 0:
            raise ValueError("Expenses cannot be negative.")
        budget = self.get_budget(category)
        return budget - expenses

    def total_budget(self) -> float:
        """
        Get the total budget across all categories.

        :return: The sum of all budgeted amounts.
        """
        return sum(self.budgets.values())

    def __str__(self) -> str:
        """
        Return a string representation of budgets in all categories.

        :return: A string displaying the budgets for all categories.
        """
        return " | ".join(f"{cat}: ${amt}" for cat, amt in self.budgets.items())
