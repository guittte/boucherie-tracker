from flask import Blueprint, jsonify, request

users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    # Logic for user registration (e.g., save to DB, hash password)
    return jsonify({"message": "User registered successfully", "user_email": data.get('email')}), 201

@users_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    # Logic for user login (e.g., verify credentials, generate JWT)
    return jsonify({"message": "User logged in successfully", "token": "dummy_jwt_token"}), 200

@users_bp.route('/profile/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    # Logic to fetch user profile
    return jsonify({"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com"}), 200
