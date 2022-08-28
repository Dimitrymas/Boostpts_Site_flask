from flask import request, render_template, redirect, flash, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from midllewares.sendEmail import send_confirm_email

from models.model import User, Orders
from sweater import db, app


class UserPage:
    def register_page():
        print("register_page")
        return render_template('register.html')


    def register():
        if current_user.is_authenticated:
            return redirect('/')
        print("register")
        login = request.form.get("login")
        email = request.form.get("email")
        first_name = request.form.get("firstname")
        last_name = request.form.get("lastname")
        password = request.form.get("password")
        password2 = request.form.get("password2")


        if not (login or first_name or last_name or password or password2 or email):
            flash('please fill forms')
        elif password != password2:
            flash('Password is not equal!')
        else:
            try:
                fullname = first_name + " " + last_name
                hash_pwd = generate_password_hash(password)
                email_token= generate_password_hash(email)
                print("f",email_token)
                new_user = User(username=login.lower(), name=fullname, email=email, password=hash_pwd, email_token=email_token)
                db.session.add(new_user)
                db.session.commit()
                print("db",new_user.email_token)
            except:

                flash(f'The {login} already taken')
            send_confirm_email(email, email_token, "confirm")
            print("s",email_token)
            return redirect(url_for('user_bp.login_page'))


    def login_page():
        if current_user.is_authenticated:
            return redirect('/')
        print("login_page")
        login = request.form.get("login")
        password = request.form.get("password")
        print(login, password)
        if login and password:
            user = User.query.filter_by(username=login.lower()).first()
            if user and check_password_hash(user.password, password):
                if  user.active:
                    login_user(user)

                    next_page = request.args.get('next')
                    if next_page == None:
                        return redirect(url_for('base_bp.home'))
                    return redirect(next_page)
                else:
                    flash('Confirm your email')
            else:
                flash('Wrong password')
        else:
            flash('Please fill forms')
        return render_template('login.html')

    @login_required
    def profile():
        order = []
        if current_user.role == "BOOSTER":
            order = Orders.query.filter_by(executor=current_user.username).all()
        elif current_user.role == "USER":
            order = Orders.query.filter_by(username=current_user.username).all()
        elif current_user.role == "ADMIN":
            order = Orders.query.all()

        print(order)
        username = current_user.username
        user = User.query.filter_by(username=username).first()
        return render_template('profile.html', user=user, orders=order)

    def email_confirm(email_token):
        print(email_token)
        user = User.query.filter_by(email_token=email_token).first()
        print(user)
        user.active = True
        user.email_token = None
        db.session.commit()

        return redirect("/user/login")

    def repass_page():
        return render_template("repass_email.html")

    def repass():
        email = request.form.get("email")
        if not email:
            flash("Please fill form")

        user = User.query.filter_by(email=email).first()
        if user:
            email_token = generate_password_hash(email)
            user.email_token = email_token
            db.session.commit

            send_confirm_email(email, email_token, "repass")



    def repass_token_page(email_token):
        return render_template("repass_password")

    def repass_token(email_token):
        password = request.form.get("password")
        user = User.query.filter_by(email_token=email_token).first()
        user.password = password
        user.email_token = None
        db.session.commit
        return redirect("/user/login")


    @login_required
    def logout():
        logout_user()
        return redirect('/')

    @app.after_request
    def redirect_to_signin(response):
        if response.status_code == 401:
            return redirect(url_for('user_bp.login_page') + '?next=' + request.url)
        return response

