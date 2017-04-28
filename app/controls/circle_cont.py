#The following file defines mod_user, a blueprint instance.
#All user related routes will be defined as mod_user from now on.

from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from sqlalchemy.orm import load_only              

from app.models.user_mod import User
from app import db

mod_user = Blueprint('circle', __name__)


#The following route takes a user id and returns a HTML page corresponding 
# to all the circles followed by that user.
@mod_user.route('/circle/<handle>')
def viewprofile(handle):
	user= Circle.query.filter_by(handle=handle).first()
	return render_template("circle.html",user=user)


    
                
