from flask import Blueprint
from controllers.buy_controller import BuyPage

buy_bp = Blueprint('buy_bp', __name__)

buy_bp.route('/buy', methods=['GET'])(BuyPage.Buy)
buy_bp.route('/buy', methods=['POST'])(BuyPage.Buy)
