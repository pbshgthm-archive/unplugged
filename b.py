from base64 import b64encode
from a import User,Article,Circle

users = 0
articles = 0
circles = 0

def addUser(name,email,password,interests,profile_pic,cover_pic,handle=''):
    new = User(++users,name,email,password,interests,profile_pic,cover_pic,handle)
    db.session.add(new)
    db.session.commit()

def createCircle(name,creator,setting):  #0 = public 1 = permissions
    new = Circle(++circles,creator,name,setting)
    db.session.add(new)
    db.session.commit()

def createArticle():
    pass
    
                
