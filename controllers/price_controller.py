from flask import session, url_for, render_template, request, redirect

class PricePage:
    def price():
            return render_template('Price.html')

    def buy_in_price():
        serv = request.form.get('serv_type')
        return redirect(url_for('buy_bp.Buy', type=serv))

