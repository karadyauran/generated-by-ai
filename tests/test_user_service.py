import unittest
from unittest.mock import MagicMock
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

class TestUserService(unittest.TestCase):
    """
    Unit tests for the User Service.
    """

    def setUp(self):
        """Set up the UserService with a mocked repository."""
        self.mock_repo = MagicMock(spec=UserRepository)
        self.user_service = UserService(self.mock_repo)

    def test_get_all_users(self):
        """Test retrieving all users."""
        self.mock_repo.get_all_users.return_value = []
        users = self.user_service.get_all_users()
        self.assertEqual(users, [])

    def test_get_user_by_id(self):
        """Test retrieving a user by ID."""
        user_id = 1
        self.mock_repo.get_user_by_id.return_value = None
        user = self.user_service.get_user_by_id(user_id)
        self.assertIsNone(user)

    def test_add_user(self):
        """Test adding a new user."""
        user_data = {}
        self.mock_repo.add_user.return_value = MagicMock(to_dict=lambda: user_data)
        new_user = self.user_service.add_user(user_data)
        self.assertEqual(new_user, user_data)

    def test_update_user(self):
        """Test updating an existing user."""
        user_id = 1
        updated_data = {}
        self.mock_repo.update_user.return_value = MagicMock(to_dict=lambda: updated_data)
        updated_user = self.user_service.update_user(user_id, updated_data)
        self.assertEqual(updated_user, updated_data)

    def test_delete_user(self):
        """Test deleting a user by ID."""
        user_id = 1
        self.mock_repo.delete_user.return_value = True
        result = self.user_service.delete_user(user_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()