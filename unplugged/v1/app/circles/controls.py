from flask import Blueprint, request, render_template, \
   
                  flash, g, session, redirect, url_for

from app.circles.models import Circle



mod_users = Blueprint('circle', __name__)


@mod_users.route('/????', methods=['GET'])
def createCircle(name,creator,setting,handle=''):  #0 = public 1 = permissions
    err = valid_circle(name,handle)
    if not err:
        new = Circle(creator,name,setting)
        db.session.add(new)
        db.session.commit()
        return new
    else:
        return err


    
    
                
