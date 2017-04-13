from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from sqlalchemy.orm import load_only

from app.models.user_mod import User
from app import db

mod_user = Blueprint('users', __name__)


@mod_user.route('/<handle>')
def viewprofile(handle):
	user= User.query.filter_by(handle=handle).first()
	return render_template("profile.html",user=user)

@mod_user.route('/allusers')
def allusers():
	users= User.query.all()
	user_list=[{"id":i.id,"handle":i.handle,"name":i.name} for i in users]
	return jsonify(user_list)
