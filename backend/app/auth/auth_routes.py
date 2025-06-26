from flask import Blueprint, request, jsonify
from .auth_controller import AuthController

auth_bp = Blueprint('auth', __name__, url_prefix='/auth/')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user_login = AuthController.login(username=username, password=password)
    return jsonify(user_login), user_login['status_code']