from flask import Blueprint
from controllers.orders_controller import OrderPage

order_bp = Blueprint('order_bp', __name__)


order_bp.route('/all', methods=['GET'])(OrderPage.orders_page)

order_bp.route('/takeconfirmorder<id>', methods=['GET'])(OrderPage.take_order_confirm_page)
order_bp.route('/takeconfirmorder<id>', methods=['POST'])(OrderPage.take_order_confirm)


