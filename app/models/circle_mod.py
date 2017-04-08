from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only

class Circle(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    name = db.Column(db.String)
    handle = db.Column(db.String,unique = True)
    tagline = db.Column(db.String)
    about = db.Column(db.String)
    canvas = db.Column(db.PickleType)
    members = db.Column(db.PickleType)
    requests = db.Column(db.PickleType) 
    archived = db.Column(db.PickleType)
    picture=db.Column(db.String)

    def __init__(self,name,handle,tagline,
        about,picture):

        
        self.name = name
        self.handle = handle
        self.tagline = tagline
        self.about = about
        self.canvas = []
        self.members = []
        self.requests = []
        self.archived = []
        self.picture=picture
        
        
    def __repr__(self):
        return "{id : %r, name: %r ,handle: %r,\
        tagline: %r , about: %r\
        }"%(self.id,self.name,self.handle,self.tagline,
            self.about)


