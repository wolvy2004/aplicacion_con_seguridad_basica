from .estudiante_model import EstudianteModel as Estudiante
from ..materia.materia_model import MateriaModel as Materia
from ..carrera.carrera_model import CarreraModel as Carrera

class EstudianteController:
    
    @staticmethod
    def get_all():
        return Estudiante.get_all()
    
    @staticmethod
    def get_one(id:int):
        estudiante = Estudiante(id=id)
        return estudiante.get_one()
    
    @staticmethod
    def create(data:dict):
        
        materias_ids = data['materias'] ## es igual a {1,8,7} lista de ids de materias
        carrera = Carrera(id=data['carrera_id'])
        materias = []
        for materia in materias_ids:
            mat = Materia(id=materia)
            materias.append(mat)
        data['materias'] = materias
        data['carrera'] = carrera
        estudiante = Estudiante(nombre_y_apellido=data['nombre_y_apellido'], carrera=data['carrera'], materias=data['materias']).create()
        return estudiante
        
        
        pass
    @staticmethod
    def update(data:dict):
        materias_ids = data['materias'] ## es igual a {1,8,7} lista de ids de materias
        carrera = Carrera(id=data['carrera_id'])
        materias = []
        for materia in materias_ids:
            mat = Materia(id=materia)
            materias.append(mat)
        data['materias'] = materias
        data['carrera'] = carrera
        del data['carrera_id']
        print(data)
        estudiante = Estudiante.deserializar(data).update()
        return estudiante
    
    @staticmethod
    def delete(id:int):
        estudiante = Estudiante(id=id).delete()
        return estudiante