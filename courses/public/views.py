# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session, make_response)

from ast import literal_eval

from courses.public.forms import SearchForm
from courses.public.umn import get_courses, get_classes
from courses.utils import flash_errors
from courses.database import db


blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/")
def home():
    return render_template("public/home.html")

@blueprint.route("/about/")
def about():
    return render_template("public/about.html")

@blueprint.route("/course/", methods=["GET", "POST"])
@blueprint.route("/course/search/", methods=["GET", "POST"])
def course_search():
    course_number = None
    compare = None
    form = SearchForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        campus = form.campus.data
        subject = form.subject.data
        level = form.level.data
        if form.course_number:
            course_number = form.course_number.data
            compare = form.compare.data

        
        session['class_search'] = False
        session['course_number'] = course_number
        session['compare'] = compare
        session['campus'] = campus
        session['subject'] = subject
        session['level'] = level
        
        return redirect(url_for('.results'))

    else:
        flash_errors(form)
    return render_template("public/search.html", form=form, class_search=False)

@blueprint.route("/class/", methods=["GET", "POST"])
@blueprint.route("/class/search/", methods=["GET", "POST"])
def class_search():
    course_number = None
    compare = None
    form = SearchForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        campus = form.campus.data
        term = form.term.data
        subject = form.subject.data
        level = form.level.data
        if form.course_number:
            course_number = form.course_number.data
            compare = form.compare.data

        
        session['class_search'] = True
        session['course_number'] = course_number
        session['compare'] = compare
        session['campus'] = campus
        session['subject'] = subject
        session['term'] = term
        session['level'] = level
        
        return redirect(url_for('.results'))

    else:
        flash_errors(form)
    return render_template("public/search.html", form=form, class_search=True)

@blueprint.route("/results/")
def results():
    abbreviations = { 'UMNTC': 'Twin Cities', 'UMNRO': 'Rochester', 'UMNCR': 'Crookston',
                       'UMNMO': 'Morris', 'UMNDL': 'Duluth'}
    semesters = { '3': 'Spring', '5': 'Summer', '9': 'Fall'}
    instructor_modes = { 'P': 'In Person, Term Based', 'ID': 'Independent/Directed Study',
                         'CE': 'Online Distance Learning', 'PA': 'Partially Online',
                         'CO': 'Completely Online', 'PR': 'Primarily Online' }

    error = False
    courses = None
    semester = None
    term = None
    campus_abr = str(session['campus'])
    campus_abr = campus_abr.upper()
    subject = session['subject']
    year = None
    class_search = session['class_search']
    course_number = session['course_number']
    compare = session['compare']
    level = session['level']

    if class_search:
        term = session['term']
        data = get_classes(campus_abr, term, level, subject, course_number, compare)
    else:
        data = get_courses(campus_abr, level, subject, course_number, compare)

    if not data:
        error = True
    else: 
        courses = data['courses']
        term_id = data['term']['term_id']
        year = '20' + term_id[1:3]
        semester = semesters[term_id[3]]
        campus = abbreviations[campus_abr]
        subject = courses[0]['subject']['description']

    return render_template("public/results.html",
                           courses=courses, 
                           year=year, 
                           semester=semester,
                           campus=campus,
                           subject=subject,
                           error=error,
                           class_search=class_search)
