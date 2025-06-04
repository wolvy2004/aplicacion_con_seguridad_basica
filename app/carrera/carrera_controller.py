from .carrera_model import CarreraModel


class CarreraController:

    @staticmethod
    def getAll():
        return CarreraModel.get_all()

    @staticmethod
    def getOne(id: int):
        carrera = CarreraModel(id=id)
        return carrera.get_one()

    @staticmethod
    def create(data: dict):
        carrera = CarreraModel(
            nombre=data['nombre'], duracion=data['duracion'])
        return carrera.create()

    @staticmethod
    def update(data: dict):
        carrera = CarreraModel(id=data['id'],
                               nombre=data['nombre'], duracion=data['duracion'])
        return carrera.update()

    @staticmethod
    def destroy(id: int):
        carrera = CarreraModel(id=id)
        return carrera.delete()
