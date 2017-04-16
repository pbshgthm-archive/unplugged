import os
from flask import *
from sqlalchemy.orm import load_only              
from werkzeug.utils import secure_filename
from app.models.canvas_mod import Article,Comment
from app.models.user_mod import User
from app import db
from config import *
from random import random

'''Important things about this file:------------------------------------------------

1)My convention for all functions: All lowercase, individual words separated by '_'
2)My convention for all the routes: camelCase
3)Important:
Whenever you want to add, edit or view an article, make the following ajax call:
$.ajax({
        url: "http://127.0.0.1:8000/canvas",
        data: {user_id:<user_id>, article_id:<article_id>},
        type: 'POST', 
        success: function(){whatever you want}
    });
user_id is the id of the user requesting the page.
Now, when you want to add article, it doesnt exist, so you dont have to send any
article_id. 
-------------------------------------------------------------------------------------'''

'''Still remaining to do--------------------------------------------------------------

1) Add some security while initialising the article.
2) Put a default picture
-------------------------------------------------------------------------------------'''

#Important variables:-----------------------------------------------------------------
mod_article = Blueprint('articles', __name__)
mod_comment = Blueprint('comments', __name__)
secret_key = ""
script_for_picture_upload_and_submit = '''
$("#done").html("<button id="done"> done </button>");
$("#input_image").html("<input id='image' type='file' name='file' />");
'''


#-------------------------------------------------------------------------------------





#All the helper functions:-------------------------------------------------------------

def initialise_article(user_id):
    user_id = user_id
    title = "Your title goes here"
    content = "Happy Writing!"
    #for now, will change later:
    picture_location = "A picture goes here"

    article_instance = Article(user_id, title, content, picture_location)
    db.session.add(article_instance)
    db.session.commit()

    return article_instance.article_id

def user_logged_in(user_id):
    #if user is in session dictionary, return true, else return false.
    #Will implement once I have the session dictionary
    return True

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def generate_secret_key():
    #can be improved
    return random()
    

#-----------------------------------------------------------------------------------------






#The routed functions (is that what they are called?):------------------------------------

@mod_article.route('/canvas/secret' , methods = ['GET','POST'])

def canvas_secret():
    
#--------------------------------GET----------------------------------------------------    
    if request.method=="GET":
        
        response = {}
        article_id = request.args["article_id"]
        current_article=Article.query.filter_by(article_id=article_id).first()

        
        if user_logged_in(current_article.user_id):
            global secret_key
            secret_key = generate_secret_key()

            response[secret_key] = secret_key
            response[edit] = "true"
            response[script] = script_for_picture_upload_and_submit;

        else:
            response[edit] = "false"
        
        article_dict = dict((col, getattr(Article, col)) for col in Article.__table__.columns.keys())
        response.update(article_dict)

        return jsonify(response)

#----------------------------POST------------------------------------------------------
    else:
        secret_key_got_back = request.form["secret_key"]
        if (secret_key_got_back!=secret_key):
            return "error"
        
        else:
            current_article.content = request.form["content"]
            current_article.title = request.form["title"]
            
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
            return "success"

# @mod_article.route('/canvas',methods = ['POST'])
# def canvas_renderer():
#     user_id = request.form["user_id"]
#     article_id = request.form["article_id"]

#testing purposes
@mod_article.route('/canvas/<article_id>',methods = ['GET'])
def canvas_renderer():
    user_id = request.args["user_id"]
    article_id = request.args["article_id"]
    print("USER ID", user_id, "  ARTICLE_ID ",article_id)
    #if article does not exist
    if (article_id == None):
        print("NO ARTICLE!!!!!!!!!!!!!")
        article_id = initialise_article(user_id)
    else:
        print(article_id)

    return render_template("canvas.html",article_id = article_id)


@mod_article.route('/canvas', methods = "GET")

#-----------------------------------------------------------------------------------------




