from flask import Flask
from base64 import b64encode
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config.from_object('config')
db = SQLAlchemy(app)



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

