from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only
from sqlalchemy.ext import mutable
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    name = db.Column(db.String)
    handle = db.Column(db.String,unique = True)
    password = db.Column(db.String)
    tagline = db.Column(db.String)
#    about = db.Column(db.String)
    email = db.Column(db.String,unique= True)
    place = db.Column(db.String)
    canvas = db.Column(db.LargeBinary)
    admin = db.Column(db.LargeBinary)
    following = db.Column(db.String)
    followers = db.Column(db.String)
    intersts=db.Column(db.LargeBinary)
    notification = db.Column(db.LargeBinary)
    archived = db.Column(db.LargeBinary)
    picture=db.Column(db.String)
    cover = db.Column(db.String)
    topic = db.Column(db.LargeBinary)
    
    def __init__(self,name,handle,password,tagline,
                 email,place,intersts,circles,picture,cover):

        self.name = name
        self.handle = handle
        self.password = password
        self.tagline = tagline
       # self.about = about
        self.email = email
        self.place=place
        self.circles = str(", 0")
        self.interests = intersts
        self.canvas = str(", 0")
        self.notification = str(", 0")
        self.archived = str(", 0")
        self.picture=picture
        self.cover = cover
        self.topic = str(", 0")
        self.admin = str(", 0")
        self.following = str(', 0')
        self.followers = str(', 0')
        
    def __repr__(self):
        return "{id : %r, name: %r ,handle: %r,\
        tagline: %r , email: %r, place: %r\
        }"%(self.id,self.name,self.handle,self.tagline,
        self.email,self.place)


