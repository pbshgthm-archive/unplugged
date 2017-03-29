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


class Feed(db.Model):
    __tablename__ = 'feeds'

    fhash = db.Column(db.String,primary_key = True)
    tstamp=db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.LargeBinary)
    link = db.Column(db.String)
    image = db.Column(db.LargeBinary)
    tag = db.Column(db.String)
    topic = db.Column(db.String)

    def __init__(self,tstamp,title,content,link,image,tag,topic):
        self.tstamp = tstamp
        self.title = title
        self.content = summary
        self.link = link
        self.image = image
        self.tag = tag
        self.topic = topic

class Archived_Feeds(db.Model):
    __tablename__ = 'feed_id'

    archived = db.relationship('Article',backref = db.backref('archived_feeds',lazy = 'dynamic'))
    id = db.Column(db.Integer, db.ForeignKey('archived.id'),unique = True)
    feeds = db.relationship('Feed',backref = db.backref('archived_feeds',lazy = 'dynamic'))
    fhash = db.Column(db.String,db.ForeignKey('feeds.fhash'),primary_key = True)

    def __init__(self,id,fhash):
        self.id = id
        self.fhash = fhash
    
db.create_all()


a = User("dsalfj","dsfljk","dfj","dfio","oifadj","dsfj")
db.session.add(a)
db.session.commit()
print(type(a.id))
b = User.query.get(a.id)
print(b)
