from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only

class Circle(db.Model):
    __tablename__ = 'circles'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    name = db.Column(db.String)
    handle = db.Column(db.String,unique = True)
    tagline = db.Column(db.String)
#    about = db.Column(db.String)
    canvas = db.Column(db.String)
    members = db.Column(db.String)
    requests = db.Column(db.String) 
    archived = db.Column(db.String)
    picture=db.Column(db.String)
    pic = db.Column(db.String)
    admin = db.Column(db.String)
    
    def __init__(self,name,handle,tagline,
                 picture,pic,admin):

        
        self.name = name
        self.handle = handle
        self.tagline = tagline
 #       self.about = about
        self.canvas = ","
        self.members = ","
        self.requests = ","
        self.archived = ","
        self.picture=picture
        self.pic=pic
        self.admin = admin
        
    def __repr__(self):
        return "{id : %r, name: %r ,handle: %r,\
        tagline: %r}"%(self.id,self.name,self.handle,self.tagline)


