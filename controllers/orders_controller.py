from flask import render_template, request, redirect
from flask_login import current_user
from midllewares.checkRole import checkRole
from models.model import Orders
from sweater import db

class OrderPage:
    @checkRole('BOOSTER', 'ADMIN')
    def orders_page():
        all_orders = Orders.query.all()
        print(all_orders)
        return render_template('orders.html', all_orders=all_orders)

    @checkRole('BOOSTER', 'ADMIN')
    def take_order_confirm_page(id):
        order = Orders.query.filter_by(id=id).first()
        if order.executor != None:
            return redirect('/orders/all')
        order = Orders.query.filter_by(id=id).first()

        return render_template("order_confirm_page.html", order=order)

    @checkRole('BOOSTER', 'ADMIN')
    def take_order_confirm(id):
        take_order = request.form.get("take_order")
        if take_order:
            order = Orders.query.filter_by(id=take_order).first()
            if order.executor != None:
                return redirect('/orders/all')
            order.active = 'ACCEPTED_BY_BOOSTER'
            order.executor = current_user.username
            db.session.commit()
            return redirect('/orders/all')





