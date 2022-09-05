from flask import render_template, request, redirect
from flask_login import login_required, current_user
from models.model import Orders
from sweater import db

types = ['1to5', '5to7', '7to9']
type_names = []


class BuyPage:
    @login_required
    def Buy():
        if request.args.get('type') and request.args.get('type') not in types:
            return redirect('/price')
        else:
            first, second, third = BuyPage.check_type(request)
            return render_template('buy.html', first=first, second=second, third=third)

    def get_boost():
        type = request.form.get('tovar')
        messager = request.form.get('msg')
        link = request.form.get('link')
        username = current_user.username
        print(type, messager, username, link)
        order = Orders(type=type, messager=messager, link=link, username=username)
        try:
            db.session.add(order)
            db.session.commit()
        finally:
            return redirect('/')

    def check_type(request):
        type = request.args.get('type')
        if type == '5to7':
            first = 'Boost from 5 to 7'
            second = 'Boost from 1 to 5'
            third = 'Boost from 7 to 9'
        elif type == '7to9':
            first = 'Boost from 7 to 9'
            second = 'Boost from 1 to 5'
            third = 'Boost from 5 to 7'
        else:
            first = 'Boost from 1 to 5'
            second = 'Boost from 5 to 7'
            third = 'Boost from 7 to 9'
        return first, second, third
