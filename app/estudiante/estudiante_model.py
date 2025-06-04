from ..database import Connect
from ..carrera.carrera_model import CarreraModel as Carrera
from ..materia.materia_model import MateriaModel as Materia


class EstudianteModel:

    

    def __init__(self, id: int = 0, nombre_y_apellido: str = "", carrera: Carrera = None, materias: list[Materia] = None):
        self.id = id
        self.nombre_y_apellido = nombre_y_apellido
        self.carrera = carrera
        self.materias = materias
        
    def serializar(self)->dict:
                   
        return {
            'id':self.id,
            'nombre_y_apellido':self.nombre_y_apellido,
            'carrera': self.carrera.serializar(),
            'materias':[materia.serializar() for materia in self.materias ] 
        }
        pass
    @staticmethod
    def deserializar(data:dict) -> 'EstudianteModel':
        return EstudianteModel(
            **data
        )
        
        """ print(data)
        return EstudianteModel(
            id=data.get('id', 0 ), 
            nombre_y_apellido=data.get("nombre_y_apellido", ""), 
            carrera=data.get('carrera', None), 
            materias=data.get('materias', None)
        )
        """
        
        
    @staticmethod
    def get_all()->list[dict]:
        cnx = Connect.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            sql="SELECT * FROM estudiantes";
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                estudiantes:list = []
                for row in result:
                    carrera = Carrera(row['carrera_id']).get_one()
                    materias = EstudianteModel.deserializar({'id':row['id']}).get_materias()
                    sql = "SELECT materia_id from estudiantes_materias where estudiante_id= %s"
                    params =(row['id'],)
                    cursor.execute(sql, params)
                    result = cursor.fetchall()
                    #materias = list(map(lambda  materia: Materia(id=materia['materia_id']).get_One() , result))
                    #print(f" mapeo de materias: {materias}")
                    row['materias'] = materias
                    row['carrera'] = carrera
                    del row['carrera_id']
                    estudiantes.append(row)
                cnx.close()
                return estudiantes
        
    def get_one(self)->dict:
        sql = "SELECT * FROM estudiantes where id=%s"
        params = (self.id,)
        result= Connect.read(sql, params)
        if result:
            for row in result:
                id = row['id']
                carrera = Carrera.deserializar({'id':row['carrera_id']}).get_one()
                materias = EstudianteModel.deserializar({'id':id}).get_materias()
                row['carrera'] = carrera
                del row['carrera_id']
                row['materias']= materias
            return row
                
    def create(self):
        try:
            sql = " INSERT INTO estudiantes (nombre_y_apellido, carrera_id) values (%s, %s)"
            params = (self.nombre_y_apellido, self.carrera.id)
            self.id = Connect.write(sql, params)
            sql = "INSERT INTO estudiantes_materias (estudiante_id, materia_id) values (%s, $s)"
            self.add_materia()
            return True
        except Exception as e:
            return False
                
        
    def update(self):
        try:
            sql = "UPDATE estudiantes set nombre_y_apellido = %s, carrera_id = %s where id=%s"
            params= (self.nombre_y_apellido, self.carrera.id, self.id)
            result = Connect.write(sql, params)
            self.add_materia()
            return True    
        except:
            return False

    def delete(self):
        self.del_materia()
        sql = "DELETE FROM estudiantes where id=%s"
        params = (self.id,)
        result = Connect.write(sql, params)
        if result:
            return True
        else:
            return False
    
    
    def get_materias(self)->list[Materia]:
        sql = "SELECT materia_id from estudiantes_materias where estudiante_id = %s"
        """
        {materia_id:1}, {materia_id:2}
        """
        params = (self.id,)
        cnx= Connect.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
            materias = []
            if result:
                for row in result:
                    materia = Materia(row['materia_id']).get_One()
                    del materia['carrera']
                    materias.append(materia)
            return materias
                    
    def add_materia(self):
        self.del_materia()
        try:
            sql = "INSERT INTO estudiantes_materias (estudiante_id, materia_id) value(%s, %s)"
            for materia in self.materias:
                    params=(self.id, materia.id)
                    result =Connect.write(sql, params)
                    if result:
                        print("materias agregadas correctamente")
        except:
            print('error al eliminar materias')
    
    def del_materia(self):
        try:
            sql = "DELETE FROM estudiantes_materias where estudiante_id= %s"
            params= (self.id,)
            result = Connect.write(sql, params)
            if result:
                print("materias eliminadas correctamente")
        except:
          print('error al eliminar materias')
        
        