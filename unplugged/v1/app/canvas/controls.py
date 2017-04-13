from flask import Blueprint, request, render_template, \
   
                  flash, g, session, redirect, url_for

from app.Canvas.models import Article
import app.common.validate as validator


mod_users = Blueprint('article', __name__)


@mod_users.route('/??????', methods=['GET'])
def createArticle(title,content,image,author,tstamp,byline):
    new = Article(content,title,image,tstamp,author,byline)
    db.session.add(new)
    db.session.commit()
    return new
