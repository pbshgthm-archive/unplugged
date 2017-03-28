# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for
app = Flask(__name__)


from sqlalchemy import TypeDecorator
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext import mutable
from sqlalchemy.orm import sessionmaker


import os
import json
from random import shuffle


Base = declarative_base()

class Feed(Base):
	
    __tablename__ = 'feeds'

    fhash = Column(String, primary_key=True)
    tstamp=Column(Integer)
    title = Column(String)
    summary = Column(String)
    link = Column(String)
    image = Column(String)
    date = Column(String)
    tag = Column(String)
    topic = Column(String)
    fid = Column(Integer)
    
 


engine = create_engine('sqlite:///main.db')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
	


@app.route('/topic/<topic>')
def topic(topic):	
	Session=sessionmaker(bind=engine)
	session=Session()
	feeds=session.query(Feed).filter_by(topic=topic).all()
	shuffle(feeds)
	session.commit()
	path="../"
	return render_template("pro.html",feeds=feeds,path=path)


@app.route('/')
def index():
	Session=sessionmaker(bind=engine)
	session=Session()
	feeds=session.query(Feed).all()
	shuffle(feeds)
	session.commit()
	path=""
	return render_template("pro.html",feeds=feeds,path=path)


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True,threaded=True)


