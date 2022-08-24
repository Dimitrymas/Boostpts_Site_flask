from flask import Blueprint
from controllers.base_controller import BasePage

base_bp = Blueprint('base_bp', __name__)

base_bp.route('/', methods=['GET'])(BasePage.home)
