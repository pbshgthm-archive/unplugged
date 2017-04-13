# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    fid = Column(Integer, autoincrement=True)
    
 


engine = create_engine('sqlite:///main.db')
Base.metadata.create_all(engine)


def queryDB():
	
	Session=sessionmaker(bind=engine)
	session=Session()
	a=session.query(Feed).all()
	session.commit()
	
	return a






@app.route('/')
def index():
	
	feeds=queryDB()

	return render_template("pro.html",feeds=feeds)
if __name__ == '__main__':
	app.run(debug=True)


