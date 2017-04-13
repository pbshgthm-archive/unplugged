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



@app.errorhandler(404)
def handle_404(e):
    path = request.path

    # go through each blueprint to find the prefix that matches the path
    # can't use request.blueprint since the routing didn't match anything
    for bp_name, bp in app.blueprints.items():
        if path.startswith(bp.url_prefix):
            # get the 404 handler registered by the blueprint
            handler = app.error_handler_spec.get(bp_name, {}).get(404)

            if handler is not None:
                # if a handler was found, return it's response
                return handler(e)

    # return a default response
    return "NOT FOUNF", 404


app.config.from_object('config')
db = SQLAlchemy(app)







from app.controls.user_cont import mod_user
from app.controls.frame_cont import mod_frame



app.register_blueprint(mod_user)
app.register_blueprint(mod_frame)


db.create_all()


