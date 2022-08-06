from flask import Flask, render_template, request
import telebot
from telebot import types
app = Flask(__name__)
bot = telebot.TeleBot('5346358084:AAEdMwWlKwXJxpyON60TcAcjnZD62ZQ7zSo')

@app.route('/',methods = ['GET','POST'])
def index():  # put application's code here
    if request.method == 'POST':
        if request.form.get('tovar') != '':
            t = request.form.get('tovar')
            msg = request.form.get('msg')
            link = request.form.get('link')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(-1001546503841, msg + '\n' + link + '\n' + t, reply_markup=markup)
            return render_template('index.html')
    return render_template('index.html')
@app.route('/price',methods = ['GET','POST'])
def price():
    return render_template("price.html")

@app.route('/buy',methods = ['GET','POST'])
def buy():
    if request.method == 'POST':
        print(request.form.get)
        if request.form.get('action1') == 'VALUE1':
            return render_template('buy.html', first='From 1 to 5 divisions', second= 'From 5 to 7 divisions', three='From 7 to 9 divisions')
        elif request.form.get('action2') == 'VALUE2':
            return render_template('buy.html', first='From 5 to 7 divisions', second= 'From 1 to 5 divisions', three='From 7 to 9 divisions')

        elif request.form.get('action3') == 'VALUE3':
            return render_template('buy.html', first='From 7 to 9 divisions', second= 'From 1 to 5 divisions', three='From 5 to 7 divisions')
    elif request.method == 'GET':
        return render_template('buy.html', first='From 1 to 5 divisions', second= 'From 5 to 7 divisions', three='From 7 to 9 divisions')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
