from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from app import db


# Your models here
class Enrolled(db.Model):
    __tablename__ = 'enrolment'
    id = db.Column(db.Integer, primary_key = True , nullable = False)
    roll = db.Column(db.Integer, ForeignKey("students.rollno"), nullable=False)
    code = db.Column(db.Integer, ForeignKey("courses.code"), nullable=False)
    course_name = db.relationship('Course',backref="courses")

    def __init__(self,roll,code):
        self.roll = roll
        self.code = code

    def __repr__(self):
        return "<Enrollment number:%s,roll:%s,code:%s>" % (self.id, self.roll, self.code)