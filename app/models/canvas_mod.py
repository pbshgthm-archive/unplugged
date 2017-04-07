from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only
from sqlalchemy import *

class Article(db.Model):
    __tablename__ = 'articles'
    article_id = db.Column(db.Integer,primary_key=True , autoincrement = True)
    user_id = db.Column(db.Integer,  ForeignKey("users.id"))
    title = db.Column(db.String)
    content = db.Column(db.String)
    picture_location = db.Column(db.String)
    #comments = db.relationship('Comment',backref="article" ,cascade="all, delete-orphan" , lazy='dynamic')

    def __init__(self, user_id, title, content, picture_location):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.picture_location = picture_location
        
    def __repr__(self):
        return "<id: %r, title: %r>" % (self.article_id, self.title)
        

class Comment(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer,primary_key=True , autoincrement = True)
    user_id = db.Column(db.Integer,  ForeignKey("users.id"))
    article_id = db.Column(db.Integer,  ForeignKey(Article.article_id))
    content = db.Column(db.String)
    article = db.relationship(Article ,backref = 'comments')

    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return "<comment_id :%r, content: %r>" % (self.comment_id, self.content) 