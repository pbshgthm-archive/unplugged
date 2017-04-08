from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    name = db.Column(db.String)
    handle = db.Column(db.String,unique = True)
    password = db.Column(db.String)
    tagline = db.Column(db.String)
    about = db.Column(db.String)
    email = db.Column(db.String,unique= True)
    place = db.Column(db.String)
    canvas = db.Column(db.PickleType)
    circles = db.Column(db.PickleType)
    intersts=db.Column(db.PickleType)
    notification = db.Column(db.PickleType)
    archived = db.Column(db.PickleType)
    picture=db.Column(db.String)

    #changed Stringdb to String


    def __init__(self,name,handle,password,tagline,
        about,email,place,intersts,circles,picture):

        self.name = name
        self.handle = handle
        self.password = password
        self.tagline = tagline
        self.about = about
        self.email = email
        self.place=place
        self.circles = []
        self.interests = intersts
        self.canvas = []       
        self.notification = []
        self.archived = []
        self.picture=picture
        
        
    def __repr__(self):
        return "{id : %r, name: %r ,handle: %r,\
        tagline: %r , about: %r, email: %r, place: %r\
        }"%(self.id,self.name,self.handle,self.tagline,
            self.about,self.email,self.place)


