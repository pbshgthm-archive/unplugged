from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config.from_object('config')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,unique = True , autoincrement = True)
    name = db.Column(db.String)
    email = db.Column(db.String,primary_key = True)
    canvas = db.Column(db.LargeBinary)
    circles = db.Column(db.LargeBinary)
    notification = db.Column(db.LargeBinary)
    profile_pic = db.Column(db.LargeBinary)
    cover_pic = db.Column(db.LargeBinary)
    password = db.Column(db.String)
    handle = db.Column(db.String,unique = True)
  # archived = db.
    
    def __init__(self,name,email,password,intersts,profile_pic,cover_pic,handle=''):
        self.name = name
        self.password = password
        self.circles = []
        self.interests = intersts
        self.email = email
        self.canvas = []
        self.notification = []
        if handle == '':
            self.handle = '@' + email.split('@')[0] + id
        else:
            self.handle = handle
        
    def __repr__(self):
        return "User {id : %r,email: %r, name: %r }"%(self.id,self.email,self.name)

class Article(db.Model):
    __tablename__ = "reacted"
    id = db.Column(db.Integer,primary_key=True , autoincrement = True)
    content = db.Column(db.LargeBinary)
    title = db.Column(db.String)
    image = db.Column(db.LargeBinary)
    #author =
    #date = 
    #byline =
    #comments =
    #timestamp
    
    def __init__(self,id,content,title,image):
        self.id = id
        self.content = content
        self.title = title
        self.image = image

    def __repr__(self):
        return "Article {title: %r,id : %r,content: %r}"%(self.title,self.id,self.content)
    
class Circle(db.Model):
    __tablename__ = 'circles'
    id = db.Column(db.Integer,primary_key = True)
    admin = db.Column(db.LargeBinary)
    members = db.Column(db.LargeBinary)
    name = db.Column(db.String)
    requests = db.Column(db.LargeBinary)
  #  handle =
    
    def __init__(self,id,admin,name,setting):
        self.id = id
        if setting == 0:
            self.admin = list(admin)
        else:
            self.admin = []
        self.members = list(admin)
        self.name = name

    def __repr__(self):
        return "Circle {id: %r,admin: %r,members: %r,name: %r,requests: %r}"%(self.id,self.admin,self.members,self.name,self.requests)
    
db.create_all()

