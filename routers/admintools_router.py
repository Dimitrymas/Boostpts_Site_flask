from flask import Blueprint
from controllers.admintools_controller import AdminPage

admin_bp = Blueprint('admin_bp', __name__)

admin_bp.route('/', methods=['GET'])(AdminPage.admin_page)
admin_bp.route('/', methods=['POST'])(AdminPage.admin_page)

admin_bp.route('/changerole', methods=['GET'])(AdminPage.change_role_page)
admin_bp.route('/changerole', methods=['POST'])(AdminPage.change_role)
