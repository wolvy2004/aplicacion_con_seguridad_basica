from flask import Flask, Blueprint
from .carrera import carreras_bp
from .materia import materias_bp
from .estudiante import estudiantes_bp


def create_app() -> Flask:
    app = Flask(__name__)
    api_bp = Blueprint('api', __name__, url_prefix='/api_v1')
    api_bp.register_blueprint(carreras_bp)
    api_bp.register_blueprint(materias_bp)
    api_bp.register_blueprint(estudiantes_bp)
    app.register_blueprint(api_bp)
    
    return app
