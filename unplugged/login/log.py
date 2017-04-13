from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import hashlib 




#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')




pwd1=hashlib.sha1("password1".encode('utf8')).hexdigest()
pwd2=hashlib.sha1("password2".encode('utf8')).hexdigest()

user={"user1":pwd1,"user2":pwd2}


app = Flask(__name__)



@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello %s"%session['user']
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    passwd=request.form['password']
    usr=request.form['username']
    passwd=hashlib.sha1(passwd.encode('utf8')).hexdigest()
    if usr in user:
        if user[usr]==passwd:
            session['logged_in'] = True
            session['user']=usr
            return home()
        else:
            return "un-authenticated"
    else: 
        return ("username wrong")
    

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['user'] = None
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)