from flask import Blueprint, request, jsonify
from .materia_controller import MateriaController
from flask_jwt_extended import jwt_required

materias_bp = Blueprint('materia', __name__, url_prefix='/materias')


@materias_bp.route("/")
def getAllmaterias():
    materias = MateriaController.getAll()
    try:
        if materias:
            return jsonify(materias), 200
        else:
            return jsonify({'message': 'no se encontraron datos'}), 204
    except Exception as e:
        return jsonify({'message': f'error al listar {e}'}), 500


@materias_bp.route("/<int:id>")
@jwt_required()
def getOnemateria(id):
    materia = MateriaController.getOne(id)
    try:
        if materia:
            return jsonify(materia), 200
        else:
            return jsonify({'message': 'no se encontraron datos'}), 404

    except Exception as e:
        return jsonify({'message': f'error al listar {e}'}), 500


@materias_bp.route("/", methods=['POST'])
def createmateria():
    datos = request.get_json()
    materia_nueva = MateriaController.create(datos)
    try:
        if materia_nueva:
            return jsonify({'message': 'materia creada con exito'}), 201
        else:
            return jsonify({'message': 'error al crear la materia'}), 400
    except Exception as e:
        return jsonify({'message': f'error al crear {e}'}), 500


@materias_bp.route("/<int:id>", methods=['PUT'])
def updatemateria(id):
    datos = request.get_json()
    materia_update = MateriaController.update(datos)
    try:
        if materia_update:
            return jsonify({'message': 'materia modificada con exito'}), 201
        else:
            return jsonify({'message': 'materia no encontrada'}), 404
    except Exception as e:
        return jsonify({'message': f'error al modificar {e}'}), 500


@materias_bp.route("/<int:id>", methods=['DELETE'])
def deletemateria():
    materia = MateriaController.destroy(id)
    try:
        if materia:
            return jsonify({'message': 'materia eliminada con exito'}), 200
        else:
            return jsonify({'message': 'materia no encontrada'}), 404
    except Exception as e:
        return jsonify({'message': f'error al listar {e}'}), 500
