from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
    __tablename__= 'courses'
    # Define the fields here
    code = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    #is there any necessary relation i need to fill?

    def __init__(self, code, name):
        # Fill this up
        self.code = code
        self.name = name

   


