from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    phone = db.Column(db.String(15),unique=True)
    address = db.Column(db.String(150))
    #email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    status = db.Column(db.Boolean)

class Gchild(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    lastLoc = db.Column(db.String(100))
    img = db.Column(db.Text)
    mimetype =db.Column(db.Text)
    encoding = db.Column(db.LargeBinary)
    status = db.Column(db.Boolean)
    
class Unknown(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.Integer)
    name = db.Column(db.String(150))
    phone = db.Column(db.String(15))
    loc = db.Column(db.String(100))
    img = db.Column(db.Text)
    mimetype =db.Column(db.Text)
    