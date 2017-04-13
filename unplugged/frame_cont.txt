from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify



from app.models.user_mod import User
from app import db

mod_frame = Blueprint('frame', __name__)


@mod_frame.route('/')
def home():   
    return "Home"






@mod_frame.route('/profiletest')
def test():   
    user= User.query.all()[-1]
    #return jsonify(str(user))
    return render_template("profile.html",user=user)

@mod_frame.route('/circletest')
def test_cir():   
    return render_template("circle.html")


@mod_frame.route('/<handle>/canvas')
def canvas(handle):   
    user= User.query.all()[-1]
    return render_template("canvas.html",user=user)



@mod_frame.route('/usertest')
def test_usr():   
    return render_template("test.html")


@mod_frame.route('/discover')
def discover():   
    return render_template("discover.html")

@mod_frame.route('/signup',methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        name = request.form['name']   
        handle=request.form['handle']
        password=request.form['password']
        pass_conf=request.form['password_conf']
        tagline=" ...your tagline here..."
        about=".....about you....."
        email=request.form['email']
        place=request.form['place']
        intersts=""
        circles=""
        picture=request.files['photo']
        if( User.query.filter(User.email == email ).all() == [] ):
            if( password == pass_conf ):
                if( len(password) > 7 ):
                    if( User.query.filter(User.handle == handle).all() == [] ):
                        usr = User(name,handle,password,tagline,about,email,place,intersts,circles,"picture")
                        db.session.add(usr)
                        db.session.commit()
                        return "success"
                    return "handle taken"
                return"password must be atleast 8 characters long"
            return "passwords dont match"
        return "email already exists"

    return render_template("signup.html")
    
@mod_frame.route('/han',methods=['POST'])
def unique_handle():
    data = request.json
    if User.query.filter(User.handle == data['handle']).all() == []:
        return str("ok")
    return str("already taken")
                
@mod_frame.route('/email',methods=['POST'])
def unique_email():
    data = request.json
    if User.query.filter(User.email == data['email']).all() == []:
        return str("ok")
    return str("email exists")
