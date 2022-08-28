from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Boostpts:LkSd!TM5Yn3!FM3@Boostpts.mysql.pythonanywhere-services.com/pts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "PTSM@RKET"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'fortnite.pts.market@gmail.com'
app.config['MAIL_PASSWORD'] = 'nhutrctrqhnirody'
app.config['MAIL_DEFAULT_SENDER'] = 'fortnite.pts.market@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)
app.secret_key = 'PTSMARKET'

