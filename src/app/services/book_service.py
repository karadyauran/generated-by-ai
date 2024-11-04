from app.repositories.book_repository import BookRepository

class BookService:
    """
    Service layer for handling book-related operations.
    """

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def get_all_books(self):
        """Retrieve all books using the repository."""
        return [book.to_dict() for book in self.book_repository.get_all_books()]

    def get_book_by_id(self, book_id: int):
        """Retrieve a single book by its ID."""
        book = self.book_repository.get_book_by_id(book_id)
        return book.to_dict() if book else None

    def add_book(self, book_data: dict):
        """Add a new book using the repository."""
        new_book = self.book_repository.add_book(book_data)
        return new_book.to_dict()

    def update_book(self, book_id: int, book_data: dict):
        """Update an existing book's information."""
        updated_book = self.book_repository.update_book(book_id, book_data)
        return updated_book.to_dict() if updated_book else None

    def delete_book(self, book_id: int):
        """Delete a book using the repository."""
        return self.book_repository.delete_book(book_id)