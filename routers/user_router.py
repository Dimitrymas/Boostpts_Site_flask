from flask import Blueprint
from controllers.user_controller import UserPage

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/register', methods=['GET'])(UserPage.register_page)
user_bp.route('/register', methods=['POST'])(UserPage.register)

user_bp.route('/login', methods=['GET', 'POST'])(UserPage.login_page)

user_bp.route('/logout', methods=['GET', 'POST'])(UserPage.logout)

user_bp.route('/myprofile', methods=['GET', 'POST'])(UserPage.profile)

user_bp.route('/confirm/<email_token>', methods=['GET'])(UserPage.email_confirm)

