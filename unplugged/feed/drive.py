# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for
app = Flask(__name__)



import os
import json
from random import shuffle

#####################################

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext import mutable
from sqlalchemy.orm import sessionmaker
import hashlib
import traceback

import os
import json
import urllib.request



file=open("sys/feedlist")
code_list=json.load(file)

code={}
for i in code_list:
    code[code_list[i]]=i
    

#################################


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
	

def qtopic(topic):
    Session=sessionmaker(bind=engine)
    session=Session()
    return session.query(Feed).filter_by(topic=topic).all()




def all():
    Session=sessionmaker(bind=engine)
    session=Session()
    return session.query(Feed).all()
	

@app.route('/topic/<topic>')
def topic(topic):
    topic=code[topic]
    feeds=qtopic(topic)
    shuffle(feeds)
    path="../"
    return render_template("pro.html",feeds=feeds,path=path)


@app.route('/topic')
def list():
    path=""
    return render_template("list.html",topic=code_list,path=path)

@app.route('/')
def index():

	feeds=all()
	shuffle(feeds)
	path=""
	return render_template("pro.html",feeds=feeds,path=path)


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True,threaded=True)


