from .estudiante_controller import EstudianteController
from flask import Blueprint, request, jsonify

estudiantes_bp = Blueprint('estudiantes', __name__,url_prefix='estudiantes/')

@estudiantes_bp.route('/')
def get_all():
    estudiantes = EstudianteController.get_all()
    try:
        if estudiantes:
            return jsonify(estudiantes), 200
        else:
            return jsonify({'mensaje':'usuarios no encontrados'}), 404
    except Exception as e:
      return jsonify({'mensaje':f'Error {e}'}), 500
    
    
        
@estudiantes_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    estudiante = EstudianteController.get_one(id)
    try:
        if estudiante:
            return jsonify(estudiante), 200
        else:
            return jsonify({'mensaje':'usuarios no encontrados'}), 404
    except Exception as e:
      return jsonify({'mensaje':f'Error {e}'}), 500


@estudiantes_bp.route('/', methods=['POST'])
def create():
    try:
        data = request.get_json()
        estudiante = EstudianteController.create(data)
        if estudiante:
            return jsonify({'mensaje':'Estudiante creado con exito'}),201    
        else:
            return jsonify({'mensaje':'Estudiante no creado'}),404    
    except Exception as e:
        return jsonify({'mensaje': f'error al crear el usuario {e}'}),500
    
@estudiantes_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        
        estudiante = EstudianteController.update(data)
        if estudiante:
            return jsonify({'mensaje':'Estudiante modificado con exito'}),201    
        else:
            return jsonify({'mensaje':'Estudiante no encontrado'}),404    
    except Exception as e:
        return jsonify({'mensaje': f'error al modificar el usuario {e}'}),500
@estudiantes_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        estudiante = EstudianteController.delete(id)
        if estudiante:
            return jsonify({'mensaje':'Estudiante eliminado con exito'}),201    
        else:
            return jsonify({'mensaje':'Estudiante no encontrado'}),404    
    except Exception as e:
        return jsonify({'mensaje': f'error al crear el usuario {e}'}),500
      
