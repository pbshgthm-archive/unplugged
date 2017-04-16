import os
from flask import *
from sqlalchemy.orm import load_only              
from werkzeug.utils import secure_filename
from app.models.canvas_mod import Article,Comment
from app.models.user_mod import User
from app import db
from config import *


######IMAGE UPLOAD PREPROCESSING####
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/article_pictures')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#####################################


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


def editAuthenticated(user_id,article_id):
    #to be filled later
    return True

def commentAuthenticated(user_id,comment_id):
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
    
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = "picture_"+str(article_id)+".png"
        #file_abs_path = os.path.join(UPLOAD_FOLDER, filename)
        current_article.picture_location = os.path.join(UPLOAD_FOLDER, filename)
        file.save(current_article.picture_location)
    else:
        pass
        #error page that say wrong file type if wrong

    db.session.commit()
    return redirect("/"+str(current_article.article_id)+"/"+str(current_article.user_id)+"/viewArticle")

#returns the article in read only form, along with comments, and action buttons
@mod_article.route('/<article_id>/<user_id>/viewArticle' , methods=["GET"])
def viewArticle(article_id,user_id):
    article=Article.query.filter_by(article_id=article_id).first()
    user=User.query.filter_by(id=user_id).first()
    return render_template("article.html",article = article,user = user)


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

#initialises the comment and returns the comment instance
def initialise_comment(user_id, article_id):
    user_id = user_id
    article_id = article_id
    content = "My super cool pro comment!"
    
    comment_instance = Comment(user_id, article_id, content)
    db.session.add(comment_instance)
    db.session.commit()

    return comment_instance

#returns comment editor to add a new comment
@mod_comment.route("/<article_id>/<user_id>/addComment" , methods = ["GET"])
def addComment(article_id,user_id):
    comment = initialise_comment(user_id, article_id)
    return render_template("comment_editor.html" , comment = comment)

#returns comment editor with the comment already loaded
@mod_comment.route("/<user_id>/<comment_id>/editComment", methods = ["GET"])
def editComment(user_id, comment_id):
    if commentAuthenticated(user_id, comment_id):
        comment=Comment.query.filter_by(comment_id=comment_id).first()
        return render_template("comment_editor.html" ,comment = comment)
    else:
        return "Not allowed"
        # to make an arror page later

#Takes the data from the comment editor and updates the database
@mod_comment.route('/<comment_id>/editComment' , methods = ['POST']) 
def editComent(comment_id):
    current_comment=Comment.query.filter_by(comment_id=comment_id).first()
    current_comment.content = request.form["content"]
    db.session.commit()
    return redirect("/"+str(current_comment.article_id)+"/"+str(current_comment.user_id)+"/viewArticle")
    


