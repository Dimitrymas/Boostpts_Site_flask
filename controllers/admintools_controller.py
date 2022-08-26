from flask import render_template, request, redirect, url_for

from models.model import User
from sweater import db
from midllewares.checkRole import checkRole


class AdminPage:

    @checkRole('ADMIN')
    def admin_page():
        return render_template('admin.html')

    @checkRole('ADMIN')
    def change_role_page():
        role_arg = request.args.get("role")
        if role_arg == None:
            users = User.query.all()
        else:
            users = User.query.filter_by(role=role_arg)

        user_username = {}
        for user in users:
            user_username[user.username] = user.role
        return render_template('admintools.html', users_names=user_username)

    @checkRole('ADMIN')
    def change_role():
        print("change_role")
        role = request.form.get("selected_role")
        logins = request.form.getlist("selected_user")
        print(logins)
        for user in logins:
            user = user.split('--')[0]

            user = User.query.filter_by(username=user).first()
            user.role = role
            db.session.commit()

        return redirect(url_for('admin_bp.change_role_page'))


