from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.orm import load_only
from sqlalchemy.ext import mutable

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    user = db.Column(db.Integer)
    article = db.Column(db.Integer)
    comment = db.Column(db.String)

    def __init__(self,user,article,comment):
        self.comment = comment
        self.user = user
        self.article = article

    def __repr__(self):
        return "{id:%r}"%(self.id)
    
