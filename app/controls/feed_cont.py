from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify
import os


from app.models.feed_mod import Feed
from app import db
import hashlib
import json

mod_feed = Blueprint('feed', __name__)






######################################

@mod_feed.route('/feed',methods=['GET'])
def feeds():
    feeds= Feed.query.all()[:50]
    path=""
    return render_template("feed.html",feeds=feeds,path=path)

 
