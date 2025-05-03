from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User,Task,db
import jwt
import datetime
from flask import current_app

auth_bp = Blueprint('auth', __name__)

SECRET_KEY = 'naum-secret-key'

# REGISTER
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 409

    hashed_pw = generate_password_hash(password)
    new_user = User(email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# LOGIN
'''@auth_bp.route('/login', methods=['POST'])
def login():'''
@auth_bp.route('/login', methods=['POST'])
def login():
    print("🔓 login route hit")
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print("🔍 Credentials received:", email, password)

    user = User.query.filter_by(email=email).first()
    
    if user:
        print("✅ User found:", user)
        print("🔐 Stored Hash:", user.password)
        print("🧪 Password check:", check_password_hash(user.password, password))
    else:
        print("❌ No user found!")

    if not user or not check_password_hash(user.password, password):
        print("❌ Invalid credentials path hit!")
        return jsonify({'message': 'Invalid credentials'}), 403

    print("✅ Password matched")

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, current_app.config['SECRET_KEY'], algorithm='HS256')

    print("🎟️ Token:", token)
    return jsonify({'token': token}), 200

    
@auth_bp.route("/debug", methods=["GET"])
def debug_auth():
    print("🔒 auth_bp is alive!")
    return "AUTH OK", 200

    




    
    '''
    print("login route hit ")       #debugging
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    print("login attempt ",email,password)      #debugging log

    user = User.query.filter_by(email=email).first()

    print("user found ",user)       #debuggig log

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 403
    
    print("password check passed ")         #debugging log

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, current_app.config['SECRET_KEY'], algorithm='HS256')

    print("Tokem generated : ",token)

    return jsonify({'token': token}), 200
#debugging route
@auth_bp.route("/debug", methods=["GET"])
def debug_auth():
    print("🔒 auth_bp is alive!")
    return "AUTH OK", 200
    '''
