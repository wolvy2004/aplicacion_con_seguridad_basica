from flask import Blueprint, Request, jsonify
from .carrera_controller import CarreraController

carreras_bp = Blueprint('carrera', __name__, url_prefix="carreras")


@carreras_bp.route("/")
def getAllCarreras():
    carreras = CarreraController.getAll()
    try:
        if carreras:
            return jsonify(carreras), 200
        else:
            return jsonify({'message': 'no se encontraron datos'}), 204
    except Exception as e:
        return jsonify({'message': f'error al listar {e}'}), 500


@carreras_bp.route("/<int:id>")
def getOneCarrera(id):
    carrera = CarreraController.getOne(id)
    try:
        if carrera:
            return jsonify(carrera), 200
        else:
            return jsonify({'message': 'no se encontraron datos'}), 404
    except Exception as e:
        return jsonify({'message': f'error al listar {e}'}), 500


@carreras_bp.route("/", methods=['POST'])
def createCarrera():
    datos = Request.get_json()
    carrera_nueva = CarreraController.create(datos)
    try:
        if carrera_nueva:
            return jsonify({'message': 'carrera creada con exito'}), 201
        else:
            return jsonify({'message': 'error al crear la carrera'}), 400
    except Exception as e:
        return jsonify({'message': f'error al crear {e}'}), 500


@carreras_bp.route("/<int:id>", methods=['PUT'])
def updateCarrera(id):
    datos = Request.get_json()
    carrera_update = CarreraController.update(datos)
    try:
        if carrera_update:
            return jsonify({'message': 'carrera modificada con exito'}), 201
        else:
            return jsonify({'message': 'carrera no encontrada'}), 404
    except Exception as e:
        return jsonify({'message': f'error al modificar {e}'}), 500


@carreras_bp.route("/<int:id>", methods=['DELETE'])
def deleteCarrera(id):
    carrera = CarreraController.destroy(id)
    try:
        if carrera:
            return jsonify({'message': 'carrera eliminada con exito'}), 200
        else:
            return jsonify({'message': 'carrera no encontrada'}), 404
    except Exception as e:
        return jsonify({'message': f'error al listar {e}'}), 500
