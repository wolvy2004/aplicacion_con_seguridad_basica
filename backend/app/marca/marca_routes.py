from .marca_controller import MarcaController
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

marca_bp=Blueprint("marca", __name__)

@marca_bp.route("/marcas/")
def get_all():
    try:
        marcas = MarcaController.get_all()
        if marcas:
            return jsonify(marcas), 200
        else:
            return jsonify({'mensaje': 'no se encontraron marcas'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@marca_bp.route("/marcas/<int:id>")
def get_one(id):
    try:
        marca = MarcaController.get_one(id)
        if marca:
            return jsonify(marca), 200
        else:
            return jsonify({'mensaje': 'no se encontro el marca'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@marca_bp.route("/marcas/", methods=["POST"])
@jwt_required()
def crear():
    try:
        data = request.get_json()
        if data is None:
            return  jsonify({'mensaje': "no se recibieron dato"})
        result = MarcaController.crear(data)
        if result:
            return jsonify({'mensaje':'marca creado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'error al crear un marca'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
    
@marca_bp.route("/marcas/<int:id>", methods=["PUT"])
@jwt_required()
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = MarcaController.modificar(data)
        if result:
            return jsonify({'mensaje':'marca modificado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'error al modificar un marca'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500

@marca_bp.route("/marcas/<int:id>", methods=["DELETE"])
@jwt_required()
def eliminar(id):
    try:
        result = MarcaController.eliminar(id)
        if result:
            return jsonify({'mensaje':"marca eliminado con exito"}),200
        else:
            return jsonify({'mensaje':"error al eliminar un marca"}),500
    except Exception as exc:
        return jsonify({'mensaje':f"error str{exc}"})
