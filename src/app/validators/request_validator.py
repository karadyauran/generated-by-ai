from flask import request
from jsonschema import validate, ValidationError

# Example schema for a book request
book_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "published_date": {"type": "string", "format": "date"},
        "isbn": {"type": "string", "pattern": "^\d{13}$"},
        "pages": {"type": "integer", "minimum": 1},
        "cover_url": {"type": "string", "format": "uri"},
        "language": {"type": "string", "minLength": 2, "maxLength": 2}
    },
    "required": ["title", "author", "published_date", "isbn", "pages", "language"]
}

# Function to validate incoming JSON request data against a schema

def validate_request(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                validate(instance=request.json, schema=schema)
            except ValidationError as e:
                return {"error": str(e)}, 400
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage Example:
# @app.route('/some_endpoint', methods=['POST'])
# @validate_request(book_schema)
# def some_function():
#     pass