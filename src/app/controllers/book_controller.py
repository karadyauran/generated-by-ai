from flask import Blueprint, jsonify, request
from app.services.book_service import BookService

# Initialize blueprint for books
book_blueprint = Blueprint('books', __name__)

# Initialize the book service
book_service = BookService()

# Route to get all books
@book_blueprint.route('/', methods=['GET'])
def get_all_books():
    books = book_service.get_all_books()
    return jsonify(books), 200

# Route to get a book by ID
@book_blueprint.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = book_service.get_book_by_id(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

# Route to add a new book
@book_blueprint.route('/', methods=['POST'])
def add_book():
    data = request.json
    book = book_service.add_book(data)
    return jsonify(book), 201

# Route to update a book
@book_blueprint.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    updated_book = book_service.update_book(book_id, data)
    if updated_book:
        return jsonify(updated_book), 200
    return jsonify({'error': 'Update failed'}), 404

# Route to delete a book
@book_blueprint.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    success = book_service.delete_book(book_id)
    if success:
        return jsonify({'message': 'Book deleted'}), 200
    return jsonify({'error': 'Delete failed'}), 404