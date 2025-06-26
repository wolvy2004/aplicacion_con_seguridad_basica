from . import RolController
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..auth.auth_model import AuthModel
rol_bp = Blueprint('rol_routes', __name__, url_prefix="/roles")


@rol_bp.route("/", methods=['GET'])
def get_all_roles():
    try:
        roles = RolController.get_all()
        if roles:
            return jsonify(roles), 200
        else:
            return jsonify({'message': 'No se encontraron roles'}), 404
    except Exception as e:
        return jsonify({'message': f'Error al listar roles: {e}'}), 500


@rol_bp.route("/<int:id>", methods=['GET'])
def get_one_role(id):
    try:
        role = RolController.get_one(id)
        if role:
            return jsonify(role), 200
        else:
            return jsonify({'message': 'Rol no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error al obtener rol: {e}'}), 500


@rol_bp.route("/", methods=['POST'])
@jwt_required()
def create_role():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No se proporcionaron datos'}), 400
        new_role = RolController.create(data)
        if new_role:
            return jsonify({'message': 'Rol creado con éxito'}), 201
        else:
            return jsonify({'message': 'Error al crear rol'}), 400
    except Exception as e:
        return jsonify({'message': f'Error al crear rol: {e}'}), 500


@rol_bp.route("/<int:id>", methods=['PUT'])
def update_role(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No se proporcionaron datos'}), 400
        updated_role = RolController.update(id, data)
        if updated_role:
            return jsonify({'message': 'Rol actualizado con éxito'}), 200
        else:
            return jsonify({'message': 'Rol no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error al actualizar rol: {e}'}), 500


@rol_bp.route("/<int:id>", methods=['DELETE'])
def delete_role(id):
    try:
        deleted = RolController.delete(id)
        if deleted:
            return jsonify({'message': 'Rol eliminado con éxito'}), 200
        else:
            return jsonify({'message': 'Rol no encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error al eliminar rol: {e}'}), 500
