from flask import Blueprint
from controllers.price_controller import PricePage

price_bp = Blueprint('price_bp', __name__)


price_bp.route('/price', methods=['GET'])(PricePage.price)
price_bp.route('/price', methods=['POST'])(PricePage.buy_in_price)

