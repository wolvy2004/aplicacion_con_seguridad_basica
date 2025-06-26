from ..database import Connect as db


class RolModel:

    def __init__(self, id: int = 0, nombre: str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre
        }

    @staticmethod
    def deserializar(data: dict) -> "RolModel":
        return RolModel(
            id=data['id'], nombre=data['nombre']
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM roles"
        result = db.read(sql)
        if result:
            return [RolModel.deserializar(rol).serializar() for rol in result]
        else:
            return None

    def get_one(self):
        sql = "SELECT * FROM roles WHERE id = %s"
        params = (self.id,)
        result = db.read(sql, params)
        if result:
            return RolModel.deserializar(result[0]).serializar()
        else:
            return None

    def create(self):
        sql = "INSERT INTO roles (nombre) VALUES (%s)"
        params = (self.nombre,)
        result = db.write(sql, params)
        return True if result else False

    def update(self):
        sql = "UPDATE roles SET nombre = %s WHERE id = %s"
        params = (self.nombre, self.id)
        return db.write(sql, params)

    def delete(self):
        sql = "DELETE FROM roles WHERE id = %s"
        params = (self.id,)
        return db.write(sql, params)
