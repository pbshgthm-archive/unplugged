from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from sqlalchemy.orm import load_only              

from app.models.canvas_mod import Article,Comment
from app import db

mod_article = Blueprint('articles', __name__)
mod_comment = Blueprint('comments', __name__)

def initialise_article(handle):
    user_id = handle
    title = "Your title goes here"
    content = "Happy Writing!"
    #for now, will change later:
    picture_location = "A picture goes here"

    article_instance = Article(user_id, title, content, picture_location)
    db.session.add(article_instance)
    db.session.commit()

    return article_instance

def addAuthenticated(handle):
    #to be filled later
    return True


def editAuthenticated(handle,article_id):
    #to be filled later
    return True

############ARTICLE#############

#Returns the article editor after initialising the article
@mod_article.route('/<handle>/addArticle' , methods = ['GET'])
def addArticleForm(handle):
    if addAuthenticated(handle):
        article = initialise_article(handle);
        return render_template("article_editor.html" , article = article)
    else:
        return "not allowed"
        #to make an error page later

#Takes the data from the article editor and updates the database
@mod_article.route('/<article_id>/editArticle' , methods = ['POST']) 
def editArticle(article_id):
    current_article=Article.query.filter_by(article_id=article_id).first()
    current_article.title = request.form["title"]
    current_article.content = request.form["content"]
    #for now, will change later:
    current_article.picture_location = request.form["picture_location"]
    db.session.commit()
    return redirect("/"+str(current_article.article_id)+"/viewArticle")

#returns the article in read only form, along with comments, and action buttons
@mod_article.route('/<article_id>/viewArticle' , methods=["GET"])
def viewArticle(article_id):
    article=Article.query.filter_by(article_id=article_id).first()
    return render_template("article.html",article = article)


#returns the article editor along with the given article_id
@mod_article.route('/<article_id>/<handle>/editArticle', methods =['GET'] )
def editArticleForm(handle, article_id):
    if editAuthenticated(handle,article_id):
        article=Article.query.filter_by(article_id=article_id).first()
        return render_template("article_editor.html" , article = article)
    else:
        return "Not allowed"
        # to make an arror page later


########COMMENTS########

def initialise_comment(user_id, article_id):
    user_id = user_id
    article_id = article_id
    content = "My super cool pro comment!"
    
    comment_instance = Comment(user_id, article_id, content)
    db.session.add(comment_instance)
    db.session.commit()

    return comment_instance

@mod_comment.route("/<article_id>/<user_id>/addComment" , methods = ["GET"])
def addComment(article_id,user_id):
    comment = initialise_comment(user_id, article_id)
    return render_template("comment_editor.html" , article = article)

    
    
    