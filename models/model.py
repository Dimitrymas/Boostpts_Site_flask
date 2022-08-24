from sweater import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False, unique=True)
    role = db.Column(db.String(15), nullable=False, default='people')
'''
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
   # def get_id(self):
    #    return str(self.id)
'''
db.create_all()

