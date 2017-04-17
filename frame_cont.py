from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify,send_from_directory
import json

from app import app
from app.models.user_mod import User
from app.models.circle_mod import Circle
from app.models.feed_mod import Feed
from app import db
import hashlib,os


mod_frame = Blueprint('frame', __name__)
ALLOWED_EXTENSIONS = set(['jpg','jpeg','png'])

t ={'42': 'Artificial Intelligence', '43': 'Happiness', '24': 'Sports', '25': 'Spirituality', '26': 'Soccer', '27': 'Food', '20': 'Education', '21': 'Management', '22': 'Humor', '23': 'Space', '28': 'Marketing', '29': 'Interior Design', '40': 'Energy', '41': 'Brain', '1': 'love', '0': 'Relationships', '3': 'Music', '2': 'Psychology', '5': 'Math', '4': 'Medicine', '7': 'Literature', '6': 'Gaming', '9': 'Photography', '8': 'Nature', '39': 'Movies', '38': 'Motivation', '11': 'Robots', '10': 'Philosophy', '13': 'Anthropology', '12': 'Entrepreneurship', '15': 'Computer Science', '14': 'Automobiles', '17': 'Art', '16': 'Machine learning', '19': 'Books', '18': 'Gardening', '31': 'Economics', '30': 'Journalism', '37': 'Archaeology', '36': 'Physics', '35': 'Anime', '34': 'Future', '33': 'Urbanism', '32': 'Programming'}


######################################

@mod_frame.route('/',methods=["GET"])
def home():
    if 'logged_in' in session:
        if session['logged_in']:
            return redirect("/profiletest")
    return redirect("/login")
    
@mod_frame.route('/login', methods=['POST','GET'])
def do_admin_login():
    if request.method == "GET":        
        if not 'logged_in' in session or not session['logged_in']:
            return render_template("login.html")
        elif session['logged_in']:
            return redirect("/profiletest")

    passwd=request.form['password']
    usr=request.form['email']
        #  passwd=hashlib.sha1(passwd.encode('utf8')).hexdigest()
        
    a = User.query.filter(User.email == usr).all()
    if a == []:
        return jsonify({"data":"no such user"})
    if a[0].password == passwd:
        session['logged_in'] = True
        session['user']=usr
        session['id']=a[0].id
        return jsonify({"data":"success"})
    else:
        return jsonify({"data":"wrong password"})

@mod_frame.route("/logout")
def logout():
    session['logged_in'] = False
    session['user'] = None
    session['id'] = None
    return redirect("/")
        






#### TEST ###################


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

#############################

@mod_frame.route('/circletest')
def test_cir():   
    return render_template("circletest.html")


@mod_frame.route('/<handle>/canvas')
def canvas(handle):   
    user= User.query.all()[-1]
    return render_template("canvas.html",user=user)





@mod_frame.route('/discover')
def discover():   
    return render_template("discover.html")

@mod_frame.route('/create_circle',methods=['POST','GET'])
def create():
    if not 'logged_in' in session:
        return redirect("/login");
    elif not session['logged_in']:
        return redirect("/login");
    p = False
    c = False
    if request.method == 'POST':
        name=request.form['name']
        handle=request.form['handle']
        tagline=request.form['quote']
        admin = session['id']
        if 'photo' in request.files:
            picture = request.files['photo']
            if picture.filename == '' or not allowed_file_name(picture.filename):
                return jsonify({"data":"not valid image"})
            else:
                p = True
        if 'cover' in request.files:
            cover=request.files['cover']
            if  cover.filename == '':
                cover.filename == 'default.jpg';
            elif not allowed_file_name(cover.filename):
                return jsonify({"data":"not valid image"})
            else:
                c = True
        if( Circle.query.filter(Circle.handle == handle).all() == [] ):
            cir = Circle(name,handle,tagline,"","",admin)
            db.session.add(cir)
            db.session.commit()
            picture.save(os.path.join( app.config['CIRCLE_FOLDER'], str(cir.id)+'.'+picture.filename.rsplit('.', 1)[1].lower() ))
            cir.picture = str(cir.id)+'.'+picture.filename.rsplit('.', 1)[1].lower()
            if c:
                cover.save(os.path.join( app.config['CIRCLEC_FOLDER'], str(cir.id)+'.'+cover.filename.rsplit('.', 1)[1].lower() ))
                cir.pic = str(cir.id)+'.'+cover.filename.rsplit('.', 1)[1].lower()
            db.session.commit()
            d = {}
            d['data']='ok'
            d['id']=cir.id
            usr = User.query.get(session['id'])
            usr.circles = usr.circles +','+ str(cir.id)
            usr.admin = usr.admin + ',1'
            db.session.commit()
            return jsonify(d)
        else:
            return jsonify({"data":"handle exists"})
    return render_template("create_circle.html")

@mod_frame.route('/signup',methods = ['POST','GET'])
def signup():
    p = False
    c = False
    if request.method == 'POST':
        name = request.form['name']   
        handle=request.form['handle']
        password=request.form['password']
        pass_conf=request.form['password_conf']
        tagline=request.form['quote']
      #  about=".....about you....."
        email=request.form['email']
        place=request.form['place']
        intersts=""
        circles=""
        if 'photo' in request.files:
            picture=request.files['photo']
            if picture.filename == '' or not allowed_file_name(picture.filename):
                return jsonify({"data":"not valid image"})
            else:
                p = True
        if 'cover' in request.files:
            cover=request.files['cover']
            if  cover.filename == '' or not allowed_file_name(cover.filename):
                return jsonify({"data":"not valid image"})
            else:
                c = True
        if( User.query.filter(User.email == email ).all() == [] ):
            if( password == pass_conf ):
                if( len(password) > 7 ):
                    if( User.query.filter(User.handle == handle).all() == [] ):
                        usr = User(name,handle,password,tagline,email,place,intersts,circles,"","")
                        db.session.add(usr)
                        db.session.commit()
                        if p:
                            picture.save(os.path.join( app.config['UPLOAD_FOLDER'], str(usr.id)+'.'+picture.filename.rsplit('.', 1)[1].lower() ))
                        if c:
                            cover.save(os.path.join( app.config['COVER_FOLDER'], str(usr.id)+'.'+cover.filename.rsplit('.', 1)[1].lower() ))
                        usr.picture = str(usr.id) + '.' + picture.filename.rsplit('.', 1)[1].lower()
                        usr.cover =  str(usr.id) + '.' + cover.filename.rsplit('.', 1)[1].lower()
                        db.session.commit()
                        return jsonify({"data":"success"})
                    else:
                        return jsonify({"data":"handle taken"})
                else:
                    return jsonify({"data":"password must be atleast 8 characters long"})
            else:
                return jsonify({"data":"passwords dont match"})
        else:
            return jsonify({"data":"email already exists"})
    return render_template("signup.html")

    
@mod_frame.route('/han',methods=['POST'])
def unique_handle():
    data = request.json
    if User.query.filter(User.handle == data['handle']).all() == []:
        return str("ok")
    return str("already taken")

@mod_frame.route('/circle_han',methods=['POST'])
def uni_han():
    data = request.json
    if Circle.query.filter(Circle.handle == data['handle']).all() == []:
        return str("ok")
    return str("already taken")

@mod_frame.route('/email',methods=['POST'])
def unique_email():
    data = request.json
    if User.query.filter(User.email == data['email']).all() == []:
        return str("ok")
    return str("email exists")

@mod_frame.route('/update',methods=['POST'])
def update():
    if session['logged_in']:
        pass

        
@mod_frame.route('/get_data',methods=['GET'])
def get():
    if session['logged_in']:
        a = User.query.get(session['id'])
        d = {}
        d["email"] = a.email
        d["name"] = a.name
        d["handle"] = a.handle
        for i in a.canvas:
            pass
        for i in a.circles:
            pass
        return jsonify(d)
    return "plethora"


def allowed_file_name(filename):
    if filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False

@mod_frame.route('/feedi',methods=['POST'])
def feed():
    a = request.json
 #   return str(a)
    f = Feed.query.filter(Feed.topic == t[str(a['id'])]).all();
    a = []
    for i in f:
        d = {}
        d['title'] = i.title
        d['image'] = i.image
        d['summary'] = i.summary
        d['link'] = i.link
        a.append(d)
    return jsonify(a)

@mod_frame.route('/circlei',methods=['POST'])
def circlei():
    a = response.json
    c = Circle.query.get(a['id'])
    d = {}
    a = []
    for i in c.canvas[:8]:
        d = {}
        b = Feed.query.get(i)
        d['title'] = b.title
        d['link'] = b.link
        d['image'] = b.image
        d['summary'] = b.summary
        a.append(d)
    return jsonify(d)

@mod_frame.route('/secret',methods=['GET'])
def retdata():
    if 'logged_in' in session:
        if session['logged_in']:
            d = {}
            a = User.query.get(session['id'])
            d['name'] = a.name
            d['email'] = a.email
            d['handle'] = a.handle
            d['tagline'] = a.tagline
            d['place'] = a.place
            d['picture'] = a.picture
            d['cover'] = a.cover
            d['circle_image'] = []
            d['circle_id']=[]
            b = a.circles[1:-1]
            b.strip(",")
            for i in b:
                c = Circle.query.get(i)
                if c:
                    d['circle_image'].append(c.picture)
                    d['circle_id'].append(c.id)
            d['canvas_image'] = []
            d['canvas_sum']=[]
            d['canvas_meta']=[]
            d['canvas_title']=[]
            for i in a.canvas:
                pass
            #   d['topics'] = a.topic[1:-1].strip(",")
            d['topics'] = ['1','2','3','4','5','6','7']
            d['t_name'] = []
            for i in d['topics']:
                d['t_name'].append(t[i])
          #  d['topics_name'] =
            return jsonify(d)
    return redirect("/login")

@mod_frame.route('/cle',methods=['POST'])
def ret():
    a = request.json
    d = {}
    c = Circle.query.get(int(a['id']))
    if c:
        d['name'] = c.name
        d['handle'] = c.handle
        d['quote'] = c.tagline
        d['members'] = c.members.split(",")
        d['member_name'] = []
        d['mem_pic'] = []
        for i in d['members']:
            u = User.query.get(i)
            if not u== None:
                d['member_name'] = u.name
                d['mem_pic'] = u.picture
        d['canvas'] = c.canvas.split(",")
        return jsonify(d)
    return jsonify({"data":"not_found"})
    
@mod_frame.route('/circle/<int:id>',methods=['GET','POST'])
def circle(id):   
    a = Circle.query.get(id)
    if a:
        return render_template("circletest.html",id=a.id,path='../')    
    else:
        return redirect("/create_circle")
    
def fcreate():
    f = Feed("asf","sdaflkj","asflkj",1,"ljfk","sdfklj","saldfkj","sdflkj",1)
    db.session.add(f)
    db.session.commit()

@mod_frame.route("/f",methods=['GET'])
def u():
    a = []
    for i in t:
        f = Feed.query.filter(Feed.topic == t[i]).all()
        a.append(str(len(f)))
    return str(a)
