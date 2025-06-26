from ..database import Connect


class CarreraModel:

    def __init__(self, id: int = 0, nombre: str = "", duracion: int = 0):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'duracion': self.duracion
        }

    @staticmethod
    def deserializar(data: dict) -> "CarreraModel":
        return CarreraModel(
            id=data.get("id", 0), 
            nombre=data.get('nombre', ""), 
            duracion=data.get('duracion', 0)
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM carreras"
        result = Connect.read(sql)
        return result

    def get_one(self):
        sql = "SELECT * FROM carreras where id= %s"
        params = (self.id,)
        result = Connect.read(sql, params)
        return result

    def create(self):
        sql = "INSERT INTO carreras (nombre, duracion) values (%s, %s)"
        params = (self.nombre, self.duracion)
        return Connect.write(sql, params)

    def update(self):
        sql = 'UPDATE carreras set nombre = %s, duracion = %s where id = %s'
        params = (self.nombre, self.duracion, self.id)
        return Connect.write(sql, params)

    def delete(self):
        sql = "DELETE TABLE carreras where id=%s"
        params = (self.id,)
        return Connect.write(sql, params)
