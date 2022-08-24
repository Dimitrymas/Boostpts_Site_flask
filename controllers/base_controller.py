from flask import render_template


class BasePage:
    def home():
        return render_template('index.html')
