from . import RolModel as Rol


class RolController:

    @staticmethod
    def get_all():
        return Rol.get_all()

    @staticmethod
    def get_one(id: int):
        rol = Rol(id=id)
        return rol.get_one()

    @staticmethod
    def create(data: dict):
        rol = Rol(nombre=data['nombre'])
        return rol.create()

    @staticmethod
    def update(id: int, data: dict):
        rol = Rol(id=id).deserializar(data)
        return rol.update()

    @staticmethod
    def delete(id: int):
        rol = Rol(id=id)
        return rol.delete()
