from flask import render_template
from flask_login import current_user


class BasePage:
    def home():
        return render_template('index.html')
