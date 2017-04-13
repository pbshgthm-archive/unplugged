from flask_sqlalchemy import SQLAlchemy
from app import db


class Student(db.Model):
    __tablename__ = 'students'
    # Define the fields here
    name = db.Column(db.String(20) , nullable = False)
    rollno = db.Column(db.String(20), primary_key=True)
    year = db.Column(db.String(10) , nullable = False)
    courses = db.relationship('Enrolled',backref="enroll" ,cascade="all, delete-orphan" , lazy='dynamic')
    # define the courses thing here later

    def __init__(self, roll, name, year):
        # fill this up
        self.name = name
        self.rollno = roll
        self.year = year

    def __repr__(self):
        return "<Student roll:%s,name:%s,year:%s>" % (self.rollno, self.name, self.year)
