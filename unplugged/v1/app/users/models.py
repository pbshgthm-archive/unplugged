from flask import Flask
from base64 import b64encode
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config.from_object('config')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    name = db.Column(db.String)
    email = db.Column(db.String,unique= True)
    canvas = db.Column(db.PickleType)
    circles = db.Column(db.PickleType)
    notification = db.Column(db.PickleType)
    profile_pic = db.Column(db.LargeBinary)
    cover_pic = db.Column(db.LargeBinary)
    password = db.Column(db.String)
    handle = db.Column(db.String,unique = True)
    archived = db.Column(db.PickleType)
    
    def __init__(self,name,email,password,intersts,profile_pic,cover_pic,handle=''):
        self.name = name
        self.password = password
        self.circles = []
        self.interests = intersts
        self.email = email
        self.canvas = []
        self.notification = []
        self.archived = []
        if handle == '':
            self.handle = '@' + email.split('@')[0] + 'o' + str(id)
        else:
            self.handle = handle
        self.profile_pic = profile_pic
        self.cover_pic = cover_pic
        
    def __repr__(self):
        return "User {id : %r,email: %r, name: %r ,image: %r}"%(self.id,self.email,self.name,str(self.profile_pic))
