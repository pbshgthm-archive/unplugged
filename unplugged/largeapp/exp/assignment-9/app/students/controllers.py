from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.students.models import Student

mod_students = Blueprint('students', __name__)

@mod_students.route('/students',strict_slashes=False, methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return render_template('students/index.html', students=students)

@mod_students.route('/addStudent',strict_slashes=False, methods=['POST'])
def add_student():
    stu = Student(request.form["roll"], request.form["name"], request.form["year"])
    db.session.add(stu)
    db.session.commit()
    return "Student added successfully"

@mod_students.route('/addStudent')
def add_student_form():
    return render_template("/students/add_student_form.html")



   

