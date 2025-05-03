import jwt
from flask import request, jsonify
from functools import wraps
from .app import create_app
from .models import User,db,Task

SECRET_KEY = 'naum-secret-key'  # Same key used for signing

# Function to decode token and extract user ID
def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Decorator to protect routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Expecting token in Authorization header: Bearer <token>
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        user_id = decode_token(token)
        if not user_id:
            return jsonify({'message': 'Token is invalid or expired!'}), 401

        current_user = User.query.get(user_id)
        if not current_user:
            return jsonify({'message': 'User not found!'}), 404

        return f(current_user, *args, **kwargs)
    return decorated
