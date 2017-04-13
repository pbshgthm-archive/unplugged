from flask import Flask
from base64 import b64encode
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config.from_object('config')
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = "archived"
    id = db.Column(db.Integer,primary_key=True , autoincrement = True)
    content = db.Column(db.LargeBinary)
    title = db.Column(db.String)
    image = db.Column(db.LargeBinary)
    author = db.Column(db.Integer)
    tstamp = db.Column(db.DateTime)
    byline = db.Column(db.String)
    comments = db.Column(db.PickleType)
    link = db.Column(db.String)
    
    def __init__(self,content,title,image,tstamp,author,byline,link='',comments=[]):
        self.content = content
        self.title = title
        self.image = image
        self.tstamp = tstamp
        self.author = author
        self.byline = byline
        self.comments = comments
        self.link = link
        
    def __repr__(self):
        return "Article {title: %r,id : %r,content: %r}"%(self.title,self.id,self.content)
    
