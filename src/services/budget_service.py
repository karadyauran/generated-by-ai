from src.domain.budget import BudgetManager, Budget
from src.services.transaction_service import TransactionService

class BudgetService:
    """
    Service class for managing budget operations.
    """

    def __init__(self, transaction_service: TransactionService):
        self.budget_manager = BudgetManager()
        self.transaction_service = transaction_service

    def add_budget(self, category: str, limit: float):
        """
        Add a new budget or update existing one for a category.
        :param category: The category to budget.
        :param limit: Budget limit in monetary value.
        """
        self.budget_manager.add_budget(category, limit)

    def is_budget_exceeded(self, category: str) -> bool:
        """
        Check if the expenditures have exceeded the budget for a category.
        :param category: The category to check.
        :return: True if exceeded, False otherwise.
        """
        # Get total spent amount from transaction service
        total_spent = self.transaction_service.total_spent_per_category(category)
        budget = self.budget_manager.get_budget(category)
        if budget:
            budget.update_spent(total_spent)
            return self.budget_manager.check_budget_exceeded(category)
        return False

    def get_budget_report(self):
        """
        Provide a report of all categories and their budget status.
        :return: A list of budget status strings.
        """
        reports = []
        for category, budget in self.budget_manager.budgets.items():
            status = "within budget" if budget.is_within_budget() else "exceeded budget"
            report_line = (
                f"Category: {category}, Limit: {budget.limit}, "
                f"Spent: {budget.spent}, Status: {status}"
            )
            reports.append(report_line)
        return reports

    def reset_all_budgets(self):
        """
        Reset the spent amounts for all budget categories.
        """
        for budget in self.budget_manager.budgets.values():
            budget.reset_spent()