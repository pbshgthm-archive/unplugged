from flask import Blueprint, request, render_template, \
   
                  flash, g, session, redirect, url_for

from app.users.models import User
import app.common.validate as validator


mod_users = Blueprint('users', __name__)


@mod_users.route('/signup', methods=['GET'])
def addUser(name,email,password,interests,profile_pic,cover_pic,handle=''):
    err = valid_user(name,email,handle)
    if not err:
        new = User(name,email,password,interests,profile_pic,cover_pic,handle)
        db.session.add(new)
        db.session.commit()
        return new
    else :
        return err


    
    
                
