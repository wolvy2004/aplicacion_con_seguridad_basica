from .usuario_controller import UsuarioController
from flask import Blueprint, jsonify, request

usuario_bp = Blueprint("usuario", __name__, url_prefix="usuarios/")

@usuario_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    user = UsuarioController.create_user(data)
    return jsonify({'mensaje':user['mensaje']}),user['status_code']
    
    
@usuario_bp.route("/validar_username/<string:username>", methods=["GET"])    
def validarUsername(username):
    existe = UsuarioController.validar_usuario(username=username)
    if existe:
        return jsonify({'mensaje': 'el username ya existe'}),409
    else:
        return jsonify({'mensaje': 'el username no esta en uso'}),200

@usuario_bp.route("/validar_email/<string:email>", methods=["GET"])    
def validar_email(email):
    existe = UsuarioController.validar_email(email==email)
    if existe:
        return jsonify({'mensaje': 'el username ya existe'}),409
    else:
        return jsonify({'mensaje': 'el username no esta en uso'}),404
