from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify



from app.models.user_mod import User
from app import db
import hashlib


pwd1=hashlib.sha1("password1".encode('utf8')).hexdigest()
pwd2=hashlib.sha1("password2".encode('utf8')).hexdigest()

user={"user1":pwd1,"user2":pwd2}


mod_frame = Blueprint('frame', __name__)





######################################

@mod_frame.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return profiletest()
 
@mod_frame.route('/login', methods=['POST'])
def do_admin_login():
    passwd=request.form['password']
    usr=request.form['username']
    passwd=hashlib.sha1(passwd.encode('utf8')).hexdigest()
    if usr in user:
        if user[usr]==passwd:
            session['logged_in'] = True
            session['user']=usr
            session['id']='123'
            return home()
        else:
            return "un-authenticated"
    else: 
        return ("username wrong")
    

@mod_frame.route("/logout")
def logout():
    session['logged_in'] = False
    session['user'] = None
    return home()






#### TEST ###################

@mod_frame.route('/signup')
def sign():
    return render_template('signup.html')

@mod_frame.route('/secret',methods=['GET'])
def retdata():
    file=open('app/templates/xyz')
    f=file.read()
    if session['logged_in']:
        return jsonify(data=session['id'])
    return jsonify(data='GUEST')



@mod_frame.route('/profiletest',methods=['POST','GET'])
def profiletest():  

    canvas_disp=False
    if request.method == 'POST': 
        req=request.form['canvas']
        if req=='True':
            canvas_disp=True
    auth=session.get('logged_in')
    user=session['user']
    return render_template("profiletest.html",path="",auth=auth,user=user,canvas_disp=canvas_disp)

@mod_frame.route('/dashtest')
def dashtest():   
    return render_template("dashtest.html",path="")


@mod_frame.route('/canvas')
def newarticle():
    return render_template("article.html",path="",aid=-1)

@mod_frame.route('/canvas/<id>')
def extarticle(id):
    return render_template("article.html",path="../",aid=id)




@mod_frame.route('/secret/article',methods=['POST','GET'])
def secretarticle():   


    article=[1,3,5,7,9]

    if request.method=='GET':
        aid=request.args.get('articleid')
        if int(aid) in article:
            print("yes")
            title="this is title of "+aid
            tldr="summary of "+aid
            content="this is content of "+aid
            auth=False
            if int(aid) in [5,7]:
                auth=True
                print("auth")
            return jsonify({'title':title,'summary':tldr,'content':content,'image':"../static/assets/topic/fox.jpg",'auth':auth,'new':False})
        if int(aid)==-1:
            auth=True
            return jsonify({'auth':auth,'new':True})
            
        title="this is title"
        tldr="summary"
        content="this is content"

        return jsonify({'title':title,'summary':tldr,'content':content,'image':"../static/assets/topic/fox.jpg",'auth':False})        
       
    if request.method=='POST':
        title=request.json
        print(title)
        return jsonify({})



#############################

@mod_frame.route('/circletest')
def test_cir():   
    return render_template("circletest.html")






@mod_frame.route('/signup',methods = ['POST','GET'])
def signup():  
    if request.method == 'POST':
        name = request.form['name']   
        handle=request.form['handle']
        password=request.form['password']
        tagline=" ...your tagline here..."
        about=".....about you....."
        email=request.form['email']
        place=request.form['place']
        intersts=""
        circles=""
        picture="default"
        
        usr = User(name,handle,password,tagline,about,email,place,intersts,circles,picture)
        db.session.add(usr)
        db.session.commit()
        return "success"
    

    return render_template("signup.html")
    
    
                
