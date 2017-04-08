from flask import Flask, render_template

from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.controls.user_cont import mod_user
from app.controls.frame_cont import mod_frame
<<<<<<< HEAD
from app.controls.canvas_cont import mod_article, mod_comment

app.register_blueprint(mod_user)
app.register_blueprint(mod_frame)
app.register_blueprint(mod_article)
app.register_blueprint(mod_comment)
=======

app.register_blueprint(mod_user)
app.register_blueprint(mod_frame)
>>>>>>> beta

db.create_all()
