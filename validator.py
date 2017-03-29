import re
import app

def u_email(email):
   if User.query.filter(email=email):
       return 0
   return 1

def vaild_email(email):
   if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
       return 0
   return 1

def u_handle(handle):
    if User.query.filter(handle=handle):
        return 0
    return 1

def valid_handle(handle):
    if not re.match(r"@[a-zA-Z0-9]+",handle):
        return 0
    return 1

def valid_name(uname):
    if not re.match(r"[a-zA-Z0-9_]+",uname):
        return 0
    return 1


def valid_user(name,email,handle):
    if not valid_name(name):
        return 1
    elif not valid_email(email):
        return 2
    elif not u_email(email):
        return 3
    elif handle:
        if not valid_handle(handle):
            return 4
        elif not u_handle(handle):
            return 5

def u_circle_handle(handle):
    if Circle.query.filter(handle=handle):
        return 0
    return 1

def valid_circle(name,handle):
    if not valid_name(name):
        return 1
    elif handle:
        if not valid_handle(handle):
            return 4
        elif not u_circle_handle(handle):
            return 5

error = ["none","invalid name","invalid email","email exists","invalid handle","handle exists"]
    

        
        
