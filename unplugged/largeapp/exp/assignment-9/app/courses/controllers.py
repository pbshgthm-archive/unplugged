from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.courses.models import Course

mod_courses = Blueprint('courses', __name__)

@mod_courses.route('/courses', methods=['GET'])
def get_all_courses():
    
    courses = Course.query.all()
    return render_template('courses/index.html',courses = courses)
    
@mod_courses.route('/addCourse', methods=['POST'])
def add_course():
    cou = Course(request.form["code"],request.form["name"])
    db.session.add(cou)
    db.session.commit()
    return "Course added successfully"

@mod_courses.route('/addCourse')
def add_course_form():
    return render_template("/courses/add_course_form.html")
    
