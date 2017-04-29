from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify,send_from_directory
import json
import time
from app import app
from app.models.user_mod import User
from app.models.circle_mod import Circle
from app.models.feed_mod import Feed
from app.models.archive_mod import Archive
from app.models.comment_mod import Comment
from app import db
import hashlib,os


mod_frame = Blueprint('frame', __name__)
ALLOWED_EXTENSIONS = set(['jpg','jpeg','png'])

t ={'42': 'Artificial Intelligence', '43': 'Happiness', '24': 'Sports', '25': 'Spirituality', '26': 'Soccer', '27': 'Food', '20': 'Education', '21': 'Management', '22': 'Humor', '23': 'Space', '28': 'Marketing', '29': 'Interior Design', '40': 'Energy', '41': 'Brain', '1': 'love', '0': 'Relationships', '3': 'Music', '2': 'Psychology', '5': 'Math', '4': 'Medicine', '7': 'Literature', '6': 'Gaming', '9': 'Photography', '8': 'Nature', '39': 'Movies', '38': 'Motivation', '11': 'Robots', '10': 'Philosophy', '13': 'Anthropology', '12': 'Entrepreneurship', '15': 'Computer Science', '14': 'Automobiles', '17': 'Art', '16': 'Machine learning', '19': 'Books', '18': 'Gardening', '31': 'Economics', '30': 'Journalism', '37': 'Archaeology', '36': 'Physics', '35': 'Anime', '34': 'Future', '33': 'Urbanism', '32': 'Programming'}

def add(string,val):
    print(string)
    string += ", " + str(val)
    return string
def sub(string,val):
    b = string.split(", ")
    print("b")
    print(b)
    print(val)
    b.remove(val)
    print(b)
    v = []
    for i in b[1:]:
        v.append(int(i))
        print(v)
        string = ", " + str(v)[1:-1]
    if string == "":
        return ", 0"
    return string
    
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
    if not 'logged_in' in session:
        return redirect("/signup")
    if not session['logged_in']:
        return redirect("/login")
    canvas_disp=False
    if request.method == 'POST': 
        req=request.form['canvas']
        if req=='True':
            canvas_disp=True
    auth=session.get('logged_in')
    user=session.get('id')
    return render_template("profiletest.html",path="",auth=auth,user=user,canvas_disp=canvas_disp)

#############################

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

def allowed_file_name(filename):
    if filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False

@mod_frame.route('/feedi',methods=['POST'])
def feed():
    a = request.json
    f = Feed.query.filter(Feed.topic == t[str(a['id'])]).all();
    a = []
    for i in f:
        d = {}
        d['title'] = i.title
        d['image'] = i.image
        d['summary'] = i.summary
        d['link'] = i.link
        d['time'] = i.topic + "  .  " + i.date
        a.append(d)
    return jsonify(a)

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
            d['canvas_image'] = []
            d['canvas_sum']=[]
            d['canvas_meta']=[]
            d['canvas_title']=[]
            d['c_link']= []
            for i in a.archived.split(", ")[2:][::-1]:
                art = Archive.query.get(int(i))
                d['canvas_image'].append(art.image)
                d['canvas_sum'].append(art.summary)
                d['canvas_meta'].append(art.date + "  .  " + art.time)
                d['canvas_title'].append(art.title)
                d['c_link'].append(art.link)
            #   d['topics'] = a.topic[1:-1].strip(",")            
            d['topics'] = a.topic.split(", ")[2:]
            print(d['topics'])
            d['following'] = []
            d['f_image'] = []
            d['fa_id'] = []
            d['fa_title'] = []
            d['fa_sum'] = []
            d['fa_meta'] = []
            d['fa_image'] = []
            for i in a.following.split(", ")[2:]:
                user = User.query.get(int(i))
                d['following'].append(user.id)
                d['f_image'].append(user.picture)
                fa_id = []
                fa_title = []
                fa_sum = []
                fa_meta = []
                fa_image = []
                for j in user.archived.split(", ")[2::]:
                    art = Archive.query.get(int(j))
                    fa_id.append(art.id)
                    fa_title.append(art.title)
                    fa_sum.append(art.summary)
                    fa_meta.append(art.date + "  .  " + art.time)
                    fa_image.append(art.image)
                d['fa_id'].append(fa_id)
                d['fa_title'].append(fa_title)
                d['fa_sum'].append(fa_sum)
                d['fa_meta'].append(fa_meta)
                d['fa_image'].append(fa_image)
            d['t_name'] = []
            for i in d['topics']:
                d['t_name'].append(t[i])
          #  d['topics_name'] =
            return jsonify(d)
    return redirect("/login")

@mod_frame.route('/feed',methods=['GET'])
def red():
    return render_template("feeds.html",path="../");
    
@mod_frame.route('/feed/<string:id>',methods=['GET'])
def fedup(id):
    return render_template("feed.html",path="../",id=id,topic=t[str(id)])


@mod_frame.route('/addTopic',methods=['POST'])
def add_topic():
    a = request.json
    if 'logged_in' in session:
        if session['logged_in']:
            u = User.query.get(session['id'])
            if not a['id'] in u.topic.split(", "):
                u.topic = add(u.topic,a['id'])
                print("a")
            #    if u.topic == "":
           #         u.topic = a['id']
           #       else:
               
                print(u.topic)
                db.session.commit()
                return str(u.topic)
                return jsonify({"data":"success"})
            else:
                u.topic = sub(u.topic,a['id'])
                db.session.commit()
               # u.topic = u.topic[1:-1]
               # u.topic = str(u.topic[0]) + str(u.topic[1])
                return str(u.topic)
                return jsonify({"data":"success"})
    return jsonify({})

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
        print(aid)

        if aid != None:
            a = Archive.query.get(aid)
            if a:
                print("yes")
                title=a.title
                content=a.content
                auth=False
                if a.author == session['id']:
                    auth=True
                    print("auth")
            return jsonify({'title':a.title,'content':a.content,'image':"../"+a.image,'auth':auth,'new':False})
        else:
            title="this is title"
            content="this is content"
            auth=True
            return jsonify({'auth':auth,'new':True}) 

    if request.method=='POST':
        a=request.form
        b=request.files['image']
        print(a)
        if( int(a['aid']) != -1 ):
            art = Archive.query.get(int(a['aid']))
            art.content = a['content']
            art.title = a['title']
            art.time = str(time.strftime("%H:%M:%S"))
            art.date = str(time.strftime("%d:%m:%y"))
            db.session.commit()
            return jsonify({"data":"auccess","id":art.id})
                    
        else:
            if not 'image' in request.files:
                return jsonify({"data":"please upload image"})
            if b.filename == "":
                return jsonify({"data":"invalid file"})
            if not allowed_file_name(b.filename):
                return jsonify({"data":"invalid file"})
            if 'logged_in' in session:
                if session['logged_in']:
                    u = User.query.get(session['id'])
                    if(int(a['aid']) == -1):
                        art = Archive(a['title'],a['content'],str(time.strftime("%H:%M:%S")),str(time.strftime("%d:%m:%y")),"",int(session['id']))
                        db.session.add(art)
                        db.session.commit()
                        b.save(os.path.join( app.config['ARCHIVE_FOLDER'],str(art.id) + '.' + b.filename.rsplit('.', 1)[1].lower() ))
                        art.image = 'static/assets/archive/' +str(art.id) + '.' + b.filename.rsplit('.', 1)[1].lower()
                        art.link = "http://127.0.0.1:8000/canvas/" + str( art.id)
                        print(u.archived)
                        u.archived  = add(u.archived,art.id)
                        print(u.archived)
                        for i in u.followers.split(", ")[2:]:
                            a = User.query.get(int(i));
                            a.notification = add(a.notification,u.id)
                            a.notification = add(a.notification,art.id)
                        db.session.commit()
                        return jsonify({"data":"success","id":art.id,"uid":u.id})
            
                    
@mod_frame.route("/profile/<string:id>",methods=['GET'])
def pro(id):
    if 'id' in session:
        if int(id) == session['id']:
            if session['logged_in']:
                return redirect("/profiletest")
            return redirect("/login")        
    return render_template("user.html",id=id,path="../");

@mod_frame.route("/profile",methods=['POST'])
def rrr():
    u = request.json
    a = User.query.get(int(u['id']))
    print(u['id'])
    print(int(u['id']))
    if a == None:
        return jsonify({"data":"error"})
    d = {}
    d['data'] = "success"
    d['name'] = a.name
    d['email'] = a.email
    d['handle'] = a.handle
    d['tagline'] = a.tagline
    d['place'] = a.place
    d['picture'] = a.picture
    d['cover'] = a.cover
    d['canvas_image'] = []
    d['canvas_sum']=[]
    d['canvas_meta']=[]
    d['canvas_title']=[]
    d['c_link']= []
    for i in a.archived.split(", ")[2:][::-1]:
        art = Archive.query.get(int(i))
        d['canvas_image'].append(art.image)
        d['canvas_sum'].append(art.summary)
        d['canvas_meta'].append(art.date + "  .  " + art.time)
        d['canvas_title'].append(art.title)
        d['c_link'].append(art.link)
    return jsonify(d)

@mod_frame.route("/f",methods=['GET'])
def f():
    a = Feed.query.all()
    return str(len(a))

@mod_frame.route("/follow",methods=['POST'])
def follow():
    a = request.json
    u2 = User.query.get(int(a['id']))
    u = User.query.get(session['id'])
    d = {}
    if u2:
        print(u.following)
        if not int(a['id']) == int(session['id']):
            if u.following == "" or not a['id'] in u.following.split(", "):
                u.following = add(u.following,a['id'])
                
                u2.followers = add(u2.followers,str(session['id']))
                d['data'] = "success"
                d['op'] = "add"
                print(u.following)
                db.session.commit()
                return jsonify(d)
            else:
                print("a" + u2.followers)
                u.following = sub(u.following,a['id'])
                u2.followers = sub(u2.followers,str(session['id']))
                d['data'] = "success"
                d['op'] = "remove"
                print("a" + u2.followers)
                db.session.commit()
                return jsonify(d)
        return jsonify({"data":"error"})
    
@mod_frame.route("/notification",methods=['GET'])
def notify():
    if 'logged_in' in session:
        if session['logged_in']:
            user = []
            art = []
            a_link = []
            u_link = []
            d = {}
            y = 0
            u = User.query.get(session['id'])
            for i in u.notification.split(", ")[2:]:
                if y == 0:
                    a = User.query.get(int(i))
                    user.append(a.name)
                    u_link.append(a.id)
                    y = 1
                else:
                    a = Archive.query.get(int(i))
                    art.append(a.title)
                    a_link.append(a.id)
                    y = 0
                d['u_name'] = user[::-1]
                d['u_id'] = u_link[::-1]
                d['a_title'] = art[::-1]
                d['a_link'] = a_link[::-1]
                    #   d['data'] = "success"
             #   d['u_name'] = [1,2,3,4]
             #   d['u_id'] = [1,2,3,4]
             #   d["a_link"] = [1,2,3,4]
             #   d["a_title"] = [1,2,3,4]
            return jsonify(d)
        return jsonify({"data":"error"})
        
            
                    
                
