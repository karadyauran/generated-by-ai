from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    """
    Schema for serializing and deserializing User objects.
    """
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    hashed_password = fields.Str(load_only=True, required=True)
    registered_on = fields.DateTime(dump_only=True)

# Initialize schema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Usage Example:
# user_data = user_schema.dump(user_instance)
# user_instance = user_schema.load(request_data)