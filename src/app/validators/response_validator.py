from flask import jsonify
from jsonschema import validate, ValidationError

# Example schema for a book response
book_response_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "author": {"type": "string"},
        "published_date": {"type": "string", "format": "date"},
        "isbn": {"type": "string", "pattern": "^\d{13}$"},
        "pages": {"type": "integer"},
        "cover_url": {"type": "string", "format": "uri"},
        "language": {"type": "string", "minLength": 2, "maxLength": 2}
    },
    "required": ["id", "title", "author", "published_date", "isbn", "pages", "language"]
}

# Function to validate outgoing JSON response data against a schema

def validate_response(data, schema):
    try:
        validate(instance=data, schema=schema)
        return jsonify(data)
    except ValidationError as e:
        return jsonify({"error": "Response validation failed", "details": str(e)}), 500

# Usage Example:
# return validate_response(book_data, book_response_schema)