import unittest
from flask import Flask
from flask.testing import FlaskClient
from app.controllers.book_controller import book_blueprint

class TestBookController(unittest.TestCase):
    """
    Unit tests for the Book Controller.
    """

    def setUp(self):
        """Set up the test client and application context."""
        app = Flask(__name__)
        app.register_blueprint(book_blueprint, url_prefix='/api/books')
        self.client = app.test_client()

    def test_get_all_books(self):
        """Test retrieving all books."""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_id(self):
        """Test retrieving a book by ID."""
        response = self.client.get('/api/books/1')
        self.assertIn(response.status_code, [200, 404])

    def test_add_book(self):
        """Test adding a new book."""
        new_book = {
            "title": "Sample Book",
            "author": "Author Name",
            "published_date": "2023-01-01",
            "isbn": "1234567890123",
            "pages": 100,
            "cover_url": "http://example.com/cover.jpg",
            "language": "en"
        }
        response = self.client.post('/api/books/', json=new_book)
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):
        """Test updating an existing book."""
        updated_data = {"title": "Updated Title"}
        response = self.client.put('/api/books/1', json=updated_data)
        self.assertIn(response.status_code, [200, 404])

    def test_delete_book(self):
        """Test deleting a book by ID."""
        response = self.client.delete('/api/books/1')
        self.assertIn(response.status_code, [200, 404])

if __name__ == '__main__':
    unittest.main()