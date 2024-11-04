from marshmallow import Schema, fields, validate

class BookSchema(Schema):
    """
    Schema for serializing and deserializing Book objects.
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    author = fields.Str(required=True, validate=validate.Length(min=1))
    published_date = fields.Date(required=True)
    isbn = fields.Str(required=True, validate=validate.Regexp(r'^\d{13}$'))
    pages = fields.Int(required=True, validate=validate.Range(min=1))
    cover_url = fields.Url(allow_none=True)
    language = fields.Str(required=True, validate=validate.Length(equal=2))

# Initialize schema instances
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# Usage Example:
# book_data = book_schema.dump(book_instance)
# book_instance = book_schema.load(request_data)