from sweater import db, login_manager
from flask_login import UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    name = db.Column(db.String(120), nullable=False, unique=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False, unique=False)
    orders = db.Column(db.String(200), nullable=True, unique=False)
    role = db.Column(db.String(15), nullable=False, default='USER')
    email_token = db.Column(db.String(300), nullable=True, unique=False)
    active = db.Column(db.Boolean(10), nullable=False, default=False)
class Orders(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=False)
    type = db.Column(db.String(120), nullable=False, unique=False)
    active = db.Column(db.String(120), nullable=False, default="LOOKING_FOR_A_BOOSTER")
    link = db.Column(db.String(120), nullable=False, unique=False)
    messager = db.Column(db.String(120), nullable=False, unique=False)
    executor = db.Column(db.String(120), nullable=True, unique=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db.create_all()


