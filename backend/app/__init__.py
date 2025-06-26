import os
from dotenv import load_dotenv
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .carrera import carreras_bp
from .materia import materias_bp
from .estudiante import estudiantes_bp
from .usuario import usuario_bp
from .auth import auth_bp
from .rol import rol_bp
from .marca.marca_routes import marca_bp

load_dotenv()
def create_app() -> Flask:
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('FLASK_SECRET')
    CORS(app)    
    JWTManager(app)
    api_bp = Blueprint('apiv1', __name__, url_prefix='/api_v1')
    api_bp.register_blueprint(carreras_bp)
    api_bp.register_blueprint(materias_bp)
    api_bp.register_blueprint(estudiantes_bp)
    api_bp.register_blueprint(usuario_bp)
    api_bp.register_blueprint(auth_bp)
    api_bp.register_blueprint(marca_bp)
    api_bp.register_blueprint(rol_bp)
    app.register_blueprint(api_bp)
    
    return app
