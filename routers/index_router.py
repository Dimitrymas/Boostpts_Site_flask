from flask import Blueprint
from routers.buy_router import buy_bp
from routers.base_router import base_bp
from routers.price_router import price_bp
from routers.user_router import user_bp
from routers.admintools_router import admin_bp
from routers.orders_router import order_bp

def index_routers(app):

    app.register_blueprint(buy_bp, url_prefix='/')

    app.register_blueprint(admin_bp, url_prefix='/admin')

    app.register_blueprint(base_bp, url_prefix='/')

    app.register_blueprint(price_bp, url_prefix='/')

    app.register_blueprint(user_bp, url_prefix='/user')

    app.register_blueprint(order_bp, url_prefix='/orders')



