from .materia_model import MateriaModel
from ..carrera.carrera_model import CarreraModel as Carrera


class MateriaController:

    @staticmethod
    def getAll():
        return MateriaModel.get_all()

    @staticmethod
    def getOne(id: int):
        materia = MateriaModel(id=id)
        return materia.get_One()

    @staticmethod
    def create(data: dict):
        carrera = data.get('carrera_id')
        
        if carrera:
            carrer = Carrera.deserializar({"id":carrera})
            
        materia = MateriaModel(
            nombre=data['nombre'],  carrera=carrer)
        return materia.create()

    @staticmethod
    def update(data: dict):
        carrera = data.get('carrera')
        if carrera:
            carrera = Carrera.deserializar(carrera)
            data['carrera'] = carrera

        materia = MateriaModel(
            nombre=data['nombre'], duracion=data['duracion'], carrera=carrera)
        return materia.update()

    @staticmethod
    def destroy(id: int):
        materia = MateriaModel(id=id)
        return materia.delete()
