from flask import Flask
from base64 import b64encode
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config.from_object('config')
db = SQLAlchemy(app)


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
