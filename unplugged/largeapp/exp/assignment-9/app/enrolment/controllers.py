from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.enrolment.models import Enrolled

mod_report = Blueprint('enrolment', __name__)

@mod_report.route('/enroll', methods = ['POST'])
def add_student_to_course():
    enr = Enrolled(request.form["roll"],request.form["code"])
    db.session.add(enr)
    db.session.commit()
    return "Enrolment done successfully"

@mod_report.route('/enroll')
def add_student_to_course_form():
    return render_template("/enroll/enroll_student_form.html")
