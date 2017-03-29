from app import User,Article,Circle
import validator

def addUser(name,email,password,interests,profile_pic,cover_pic,handle=''):
    err = valid_user(name,email,handle)
    if not err:
        new = User(name,email,password,interests,profile_pic,cover_pic,handle)
        db.session.add(new)
        db.session.commit()
        return new
    else :
        return err
    
def createCircle(name,creator,setting,handle=''):  #0 = public 1 = permissions
    err = valid_circle(name,handle)
    if not err:
        new = Circle(creator,name,setting)
        db.session.add(new)
        db.session.commit()
        return new
    else:
        return err

def createArticle(title,content,image,author,tstamp,byline):
    new = Article(content,title,image,tstamp,author,byline)
    db.session.add(new)
    db.session.commit()
    return new

def archive_feed(fhash):
    exists = Archived_Feeds.query.get(fhash)
    if not exists:
        feed = Feed.query.get(fhash)
        new1 = Article(feed.content,feed.title,feed.image,feed.tstamp,"","",feed.link)
        db.session.add(new1)
        db.session.commit()
        new2 = Archived_Feeds(feed.fhash,new1.id)
        db.session.add(new2)
        db.session.commit()
        return new1
    return Article.query.get(exists.id)

def request_circle(cid,uid):
    circle = Circle.query.get(cid)
    user = User.query.get(uid)
    circle.requests.push(uid)
    user.requested.push(cid)

def accept_request(cid,uid,admin):
    circle.requests.remove(uid)
    circle.member.push(uid)
    user.requested.remove(cid)
    if admin:
        circle.admin.push(uid)

def delete_request(cid,uid,admin):



    
    
                
