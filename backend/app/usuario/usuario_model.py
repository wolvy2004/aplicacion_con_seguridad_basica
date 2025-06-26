from ..database import Connect
from ..rol import RolModel as Rol
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash


class UsuarioModel:
    
    def __init__(self, id:int=0, username:str="", email:str="", password:str="", rol:Rol = None):
        self.id=id
        self.username= username
        self.email = email
        self.password = password
        self.rol = rol
        
    def serializar(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            'rol':self.rol.serializar()
           
        }
    @staticmethod
    def deserializar( data:dict)->"UsuarioModel":
        return UsuarioModel(
            id=data.get("id", 0),
            username=data.get("username", ""),
            email=data.get("email", ""),
            password=data.get("password", ""),
            rol=data.get("rol", 1)
            
        )
    
    def check_password(self, password:str)->bool:
        ## chequea el password del objeto con el password 
        ## que le pasamos por parametro
        return check_password_hash(self.password, password)
        
    def set_password(self, password:str)->str:
        return generate_password_hash(password=password)
    
    def create(self):
        try:
            sql = "INSERT INTO usuarios (username, email, password, rol_id) values (%s, %s, %s, %s)"
            params = (self.username, self.email, self.set_password(self.password), self.rol.id)
            result = Connect.write(sql, params)
            if result:
                return True
        except Error as e:
                return False
            
    def get_user_by_email(email:str):
        sql = "SELECT * FROM usuarios WHERE email = %s"
        params = (email,)
        
        try:
            result = Connect.read(sql, params)
            if result:
                rol_toDict = Rol(result[0]['rol_id']).get_one() 
                result[0]['rol']=Rol.deserializar(rol_toDict)
                usuario = UsuarioModel.deserializar(result[0])
                return usuario.serializar()
            else:
                return None
        except Exception as e:
                return f"Error: {e}"
                
    def get_user_by_username(username:str):
        try:
            sql = "SELECT * FROM usuarios WHERE username = %s"
            params = (username,)
            result = Connect.read(sql, params)
            if result:
                rol_toDict = Rol(result[0]['rol_id']).get_one() 
                result[0]['rol']=Rol.deserializar(rol_toDict)
                usuario = UsuarioModel.deserializar(result[0])
                return usuario.serializar()
            else:
                return None
        except Exception as e:
                return f"Error: {e}"