from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

# Initialize blueprint for users
user_blueprint = Blueprint('users', __name__)

# Initialize the user service
user_service = UserService()

# Route to get all users
@user_blueprint.route('/', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

# Route to get a user by ID
@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# Route to add a new user
@user_blueprint.route('/', methods=['POST'])
def add_user():
    data = request.json
    user = user_service.add_user(data)
    return jsonify(user), 201

# Route to update a user
@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    updated_user = user_service.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user), 200
    return jsonify({'error': 'Update failed'}), 404

# Route to delete a user
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_service.delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'Delete failed'}), 404