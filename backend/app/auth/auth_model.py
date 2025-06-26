from ..database import Connect
from flask_jwt_extended import create_access_token
class AuthModel:
    
    @staticmethod
    def login(username:str, password:str)->dict:
        from ..usuario.usuario_model import UsuarioModel as Usuario
        from ..rol import RolModel as Rol
        username =  Usuario.get_user_by_username(username)
        print(username)
        
        if username:
            rol = Rol.deserializar(username['rol'])
            username['rol']=rol
            password = Usuario(**username).check_password(password)
        if not username or not password:
            return {'mensaje': 'credenciales invalidas', 'status_code':401}
        else:
            
            jwt = create_access_token(identity=username['username'], additional_claims={'rol':rol.nombre})
            return {
                'username': username['username'],
                'rol': rol.serializar(),
                'email': username['email'],
                'jwt':jwt,
                'status_code':200  
            }
        
    
        