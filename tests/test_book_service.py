import unittest
from unittest.mock import MagicMock
from app.services.book_service import BookService
from app.repositories.book_repository import BookRepository

class TestBookService(unittest.TestCase):
    """
    Unit tests for the Book Service.
    """

    def setUp(self):
        """Set up the BookService with a mocked repository."""
        self.mock_repo = MagicMock(spec=BookRepository)
        self.book_service = BookService(self.mock_repo)

    def test_get_all_books(self):
        """Test retrieving all books."""
        self.mock_repo.get_all_books.return_value = []
        books = self.book_service.get_all_books()
        self.assertEqual(books, [])

    def test_get_book_by_id(self):
        """Test retrieving a book by ID."""
        book_id = 1
        self.mock_repo.get_book_by_id.return_value = None
        book = self.book_service.get_book_by_id(book_id)
        self.assertIsNone(book)

    def test_add_book(self):
        """Test adding a new book."""
        book_data = {}
        self.mock_repo.add_book.return_value = MagicMock(to_dict=lambda: book_data)
        new_book = self.book_service.add_book(book_data)
        self.assertEqual(new_book, book_data)

    def test_update_book(self):
        """Test updating an existing book."""
        book_id = 1
        updated_data = {}
        self.mock_repo.update_book.return_value = MagicMock(to_dict=lambda: updated_data)
        updated_book = self.book_service.update_book(book_id, updated_data)
        self.assertEqual(updated_book, updated_data)

    def test_delete_book(self):
        """Test deleting a book by ID."""
        book_id = 1
        self.mock_repo.delete_book.return_value = True
        result = self.book_service.delete_book(book_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()