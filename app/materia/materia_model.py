from ..database import Connect
from ..carrera.carrera_model import CarreraModel as Carrera


class MateriaModel:

    def __init__(self, id: int = 0, nombre: str = "",  carrera: Carrera = None):
        self.id = id
        self.nombre = nombre
        self.carrera = carrera

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'carrera': self.carrera.serializar() if self.carrera else None
        }

    @staticmethod
    def deserializar(data: dict) -> "MateriaModel":
        return MateriaModel(
            id=data['id'], nombre=data['nombre'],  carrera=data['carrera']
        )

    @staticmethod
    def get_all() -> list[dict]:
        sql = "SELECT * FROM materias"
        result = Connect.read(sql)
        materias = []
        carreras = []
        for materia in result:
            # Obtener la carrera asociada a la materia
            carrera_toDic = Carrera(materia['carrera_id']).get_one()
            # Deserializar la carrera y agregarla al diccionario de la materia
            materia['carrera'] = Carrera.deserializar(carrera_toDic[0])
            # Serializar la materia y agregarla a la lista
            materias.append(MateriaModel.deserializar(materia).serializar())
        return materias

    def get_One(self):
        sql = "SELECT * FROM materias where id= %s"
        params = (self.id,)
        result = Connect.read(sql, params)
        if result:
            materia: dict = result[0]
            carrera = Carrera(result[0]['carrera_id']).get_one()
            materia['carrera'] = carrera
            del materia['carrera_id']
            return materia
        else:
            return result

    def create(self):
        sql = "INSERT INTO materias (nombre, carrera_id) values (%s, %s)"
        params = (self.nombre, self.carrera.id)
        return Connect.write(sql, params)

    def update(self):
        sql = 'UPDATE materias set nombre = %s, carrera_id = %s where id = %s'
        params = (self.nombre, self.carrera.id, self.id)
        return Connect.write(sql, params)

    def delete(self):
        sql = "DELETE TABLE materias where id=%s"
        params = (self.id,)
        return Connect.write(sql, params)
