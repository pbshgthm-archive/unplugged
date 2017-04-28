from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only

class Feed(db.Model):
    __tablename__ = 'feeds'
    id = db.Column(db.Integer,primary_key = True , autoincrement = True)
    title = db.Column(db.String)
    hashval = db.Column(db.String)
    link = db.Column(db.String)
    summary = db.Column(db.String)
    topic = db.Column(db.String)
    tag = db.Column(db.String)
    date = db.Column(db.String)
    image= db.Column(db.String)
    time=db.Column(db.Integer)
   # content = db.Column(db.LargeBinary)

    def __init__(self,title,hashval,link,topic,tag,date,time,summary,image):

        self.title = title
        self.hashval = hashval
        self.link = link
        self.summary = summary
        self.topic = topic
        self.tag = tag
        self.topic=topic
        self.date = date
        self.time = time
        self.image = image
       # self.content = ""

    def __repr__(self):
        return "{id : %r, title: %r ,link: %r,\
        tag: %r , date: %r, summary: %r, image: %r\
        }"%(self.id,self.title,self.link,self.tag,
            self.date,self.summary,self.image)
        
    


