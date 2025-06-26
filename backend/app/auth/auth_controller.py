from .auth_model import AuthModel as Auth

class AuthController:
    
    @staticmethod
    def login(username:str, password: str):
        if not username or not password:
            return {'mensaje': 'los datos no deben estar vacios', 'status_code':409}
        access = Auth.login(username, password)
        return access