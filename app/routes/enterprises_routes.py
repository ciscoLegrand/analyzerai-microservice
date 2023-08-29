from flask import render_template, Blueprint
from app.services.api.api_service import APIService

# Definir el Blueprint
enterprises_bp = Blueprint('enterprises', __name__, url_prefix='/enterprises')

@enterprises_bp.route('/')
def show_enterprises():
    enterprises = APIService.get_enterprises()
    return render_template('enterprises/index.html', enterprises=enterprises)

