import unittest
from flask import Flask
from flask.testing import FlaskClient
from app.controllers.user_controller import user_blueprint

class TestUserController(unittest.TestCase):
    """
    Unit tests for the User Controller.
    """

    def setUp(self):
        """Set up the test client and application context."""
        app = Flask(__name__)
        app.register_blueprint(user_blueprint, url_prefix='/api/users')
        self.client = app.test_client()

    def test_get_all_users(self):
        """Test retrieving all users."""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        """Test retrieving a user by ID."""
        response = self.client.get('/api/users/1')
        self.assertIn(response.status_code, [200, 404])

    def test_add_user(self):
        """Test adding a new user."""
        new_user = {
            "username": "sampleuser",
            "email": "sampleuser@example.com",
            "hashed_password": "hashedpassword"
        }
        response = self.client.post('/api/users/', json=new_user)
        self.assertEqual(response.status_code, 201)

    def test_update_user(self):
        """Test updating an existing user."""
        updated_data = {"username": "updateduser"}
        response = self.client.put('/api/users/1', json=updated_data)
        self.assertIn(response.status_code, [200, 404])

    def test_delete_user(self):
        """Test deleting a user by ID."""
        response = self.client.delete('/api/users/1')
        self.assertIn(response.status_code, [200, 404])

if __name__ == '__main__':
    unittest.main()