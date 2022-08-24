from flask import request, render_template, redirect, flash, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from models.model import User
from sweater import db, app


class UserPage:
    def register_page():
        return render_template('register.html')


    def register():
        login = request.form.get("login")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if not (login or password or password2):
            flash('please')
        elif password != password2:
            flash('Password is not equal!')
        else:
            hash_pwd = generate_password_hash(password)
            print(hash_pwd)
            new_user = User(username=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('user_bp.login_page'))


    def login_page():

        print()
        login = request.form.get("login")
        password = request.form.get("password")

        if login and password:
            user = User.query.filter_by(username=login).first()
            if user and check_password_hash(user.password, password):
                login_user(user)

                next_page = request.args.get('next')

                return redirect(next_page)
            else:
                flash('Wrong password')
        else:
            flash('Please fill login')
        return render_template('login.html')


    @app.after_request
    def redirect_to_signin(response):
        if response.status_code == 401:
            return redirect(url_for('user_bp.login_page') + '?next=' + request.url)
        return response

