from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only

class Archive(db.Model):
    __tablename__ = 'archive'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    title = db.Column(db.String)
    link = db.Column(db.String)
    summary = db.Column(db.String)
    topic = db.Column(db.String)
    tag = db.Column(db.String)
    date = db.Column(db.String)
    image= db.Column(db.String)
    time=db.Column(db.Integer)
    author = db.Column(db.Integer)
    comments = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self,title,content,date,time,image,author):

        self.title = title
        self.link = ""
        self.summary = content[:140] + "..."
        self.tag = ""
        self.topic=""
        self.date = date
        self.time = time
        self.image = image
        self.comments = ""
        self.author = author
        self.content = content
        
    def __repr__(self):
        return "{id : %r, title: %r ,link: %r,\
        tag: %r , date: %r, summary: %r, image: %r\
        }"%(self.id,self.title,self.link,self.tag,
            self.date,self.summary,self.image)
