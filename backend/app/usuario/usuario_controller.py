from .usuario_model import UsuarioModel as Usuario
from ..rol import RolModel as Rol
class UsuarioController:
    
    @staticmethod
    def create_user(data:dict)->bool:
        print(data)
        try:
            username,  password,email, rol = data.values()
            if not email or not username or not password or not rol:
                return {'mensaje': 'debe completar todos los campos', 'status_code':500}
            exist_username = Usuario.get_user_by_username(username)
            exist_email = Usuario.get_user_by_email(email)
            print(f' usuario encontrado por email : {exist_email}')
            
            if exist_username:
                return {'mensaje': 'error: el username ya existe', 'status_code':409}
            if exist_email:
                return {'mensaje': 'error: el email ya esta en uso', 'status_code':409}
            rol = Rol(id=rol).get_one()
            data['rol'] = Rol.deserializar(rol)
            result = Usuario(**data).create()
            if result:
                return {'mensaje': 'usuario creado con exito', 'status_code':201}
        except Exception as e:
             return {'mensaje': f'error : {e}', 'status_code':500}
    @staticmethod
    def validar_email(email:str):
        user = Usuario.get_user_by_email(email)
        return True if user else False
    @staticmethod
    def validar_usuario(username:str):
        
        user = Usuario.get_user_by_username(username)
        return True if user else False
        
            
        
        
        

