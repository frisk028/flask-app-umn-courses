# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session, make_response)

from ast import literal_eval

from courses.public.forms import SearchForm
from courses.public.umn import get_courses, get_classes
from courses.utils import flash_errors


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
    error = None
    form = SearchForm(request.form, csrf_enabled=False)
    try:
        error = session['error']
    except:
        pass
    if error:
        flash(error, 'warning')
    else:
        if form.validate_on_submit():
            campus = form.campus.data
            term = "1159"
            subject = form.subject.data
            level = form.level.data
            course_number = form.course_number.data
            compare = form.compare.data
            if campus == "umncr":
                le = form.ge.data
            elif campus == "umnmo":
                le = form.ger.data
            elif campus == "umndl":
                le = form.dle.data
            else:
                le = form.cle.data

            
            session['class_search'] = False
            session['course_number'] = course_number
            session['compare'] = compare
            session['campus'] = campus
            session['subject'] = subject
            session['term'] = term
            session['level'] = level
            session['le'] = le
            
            return redirect(url_for('.results'))

        else:
            flash_errors(form)
    session.clear()
    return render_template("public/search.html", form=form, class_search=False)

@blueprint.route("/class/", methods=["GET", "POST"])
@blueprint.route("/class/search/", methods=["GET", "POST"])
def class_search():
    form = SearchForm(request.form, csrf_enabled=False)
    error = None
    if error:
        flash(error, 'warning')
    else:
        if form.validate_on_submit():
            campus = form.campus.data
            term = form.term.data
            subject = form.subject.data
            level = form.level.data
            course_number = form.course_number.data
            compare = form.compare.data
            if campus == "umncr":
                le = form.ge.data
            elif campus == "umnmo":
                le = form.ger.data
            elif campus == "umndl":
                le = form.dle.data
            else:
                le = form.cle.data

            
            session['class_search'] = True
            session['course_number'] = course_number
            session['compare'] = compare
            session['campus'] = campus
            session['subject'] = subject
            session['term'] = term
            session['level'] = level
            session['le'] = le

            return redirect(url_for('.results'))

        else:
            flash_errors(form)
    
    session.clear()
    return render_template("public/search.html", form=form, class_search=True)

@blueprint.route("/results/")
@blueprint.route("/results/<path:path>/")
def results():
    # abbreviations = { 'UMNTC': 'Twin Cities', 'UMNRO': 'Rochester', 'UMNCR': 'Crookston',
    #                    'UMNMO': 'Morris', 'UMNDL': 'Duluth'}
    # semesters = { '3': 'Spring', '5': 'Summer', '9': 'Fall'}
    courses = None
    term = None
    campus_abr = str(session['campus'])
    campus_abr = campus_abr.upper()
    subject = session['subject']
    class_search = session['class_search']
    course_number = session['course_number']
    compare = session['compare']
    level = session['level']
    le = session['le']

    if class_search:
        term = session['term']
        data = get_classes(campus_abr, term, level, subject, course_number, compare, le)
    else:
        data = get_courses(campus_abr, level, subject, course_number, compare, le)

    if not data:
        session['error'] = 'Search too large. Please narrow down your search'
        if class_search:
            return redirect(url_for('.class_search'))
        else:
            return redirect(url_for('.course_search'))
    else:
        courses = data


    return render_template("public/results.html",
                           courses=courses,
                           class_search=class_search)
