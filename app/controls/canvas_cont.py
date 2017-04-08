from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from sqlalchemy.orm import load_only              

from app.models.canvas_mod import User,Comments
from app import db

mod_article = Blueprint('articles', __name__)
mod_comment = Blueprint('comments', __name__)

@mod_article.route('/<handle>/addArticle' , methods = ['GET'])
def addArticleForm(handle):
    if authenticated(handle):
        return render_template("article_editor.html")

@mod_article.route('/<handle>/addArticle' , methods = ['POST']) 
def addArticle(handle):
    user_id = handle
    title = request.form["title"]
    content = request.form["content"]
    #for now, will change later:
    picture_location = request.form["picture_location"]

    article_instance = Article(self, user_id, title, content, picture_location)
    db.session.add(article_instance)
    db.session.commit()

    return redirect("/"+self.article_instance.article_id+"/viewArticle")

@mod_article.route('/<article_id>/viewArticle' , methodS=["GET"])


        
