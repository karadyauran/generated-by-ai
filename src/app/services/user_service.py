from app.repositories.user_repository import UserRepository

class UserService:
    """
    Service layer for handling user-related operations.
    """

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        """Retrieve all users using the repository."""
        return [user.to_dict() for user in self.user_repository.get_all_users()]

    def get_user_by_id(self, user_id: int):
        """Retrieve a single user by their ID."""
        user = self.user_repository.get_user_by_id(user_id)
        return user.to_dict() if user else None

    def add_user(self, user_data: dict):
        """Add a new user using the repository."""
        new_user = self.user_repository.add_user(user_data)
        return new_user.to_dict()

    def update_user(self, user_id: int, user_data: dict):
        """Update an existing user's information."""
        updated_user = self.user_repository.update_user(user_id, user_data)
        return updated_user.to_dict() if updated_user else None

    def delete_user(self, user_id: int):
        """Delete a user using the repository."""
        return self.user_repository.delete_user(user_id)