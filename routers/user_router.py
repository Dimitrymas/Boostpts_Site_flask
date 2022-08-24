from flask import Blueprint
from controllers.user_controller import UserPage

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/register', methods=['GET'])(UserPage.register_page)
user_bp.route('/register', methods=['POST'])(UserPage.register)

user_bp.route('/login', methods=['GET','POST'])(UserPage.login_page)
#user_bp.route('/login', methods=['POST'])(UserPage.login)
'''
user_bp.route('/loginout', methods=['GET'])(UserPage.logout_page)
user_bp.route('/loginout', methods=['POST'])(UserPage.logout())
'''