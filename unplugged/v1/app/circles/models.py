from flask import Flask
from base64 import b64encode
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config.from_object('config')
db = SQLAlchemy(app)

    
class Circle(db.Model):
    __tablename__ = 'circles'
    id = db.Column(db.Integer,primary_key = True)
    admin = db.Column(db.PickleType)
    members = db.Column(db.PickleType)
    name = db.Column(db.String)
    requests = db.Column(db.PickleType)
    handle = db.Column(db.String,unique = True)
    
    def __init__(self,admin,name,setting,handle=''):
        if setting == 0:
            self.admin = list(admin)
        else:
            self.admin = []
        self.members = list(admin)
        self.name = name
        self.requests = []
        if handle == '':
            self.handle = '@'+self.name + 'o' + self.id
        else:
            self.handle = handle

    def __repr__(self):
        return "Circle {id: %r,admin: %r,members: %r,name: %r,requests: %r}"%(self.id,self.admin,self.members,self.name,self.requests)


