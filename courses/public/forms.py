# -*- coding: utf-8 -*-
from flask import url_for
from flask_wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired

import json

class SearchForm(Form):
    CAMPUS_CHOICES = [('umntc', 'Twin Cities'), ('umndl', 'Duluth'),
                      ('umnro', 'Rochester'), ('umncr', 'Crookston'),
                      ('umnmo', 'Morris')]

    TERM_CHOICES = [('1155', 'Summer 2015'), ('1159', 'Fall 2015'), ('1163', 'Spring 2016')]

    COMPARE_CHOICES = [('','--choose comparison--'), ('<', 'less than'), ('<=', 'less than or equal to'),
                       ('=','equal to'), ('>=', 'greater than or equal to'),
                       ('>', 'greater than')]

    LEVEL_CHOICES = [('catalog_number<5000', 'Undergraduate Courses'), 
                     ('catalog_number>4999', 'Graduate and Professional Courses')]

    campus = SelectField(label='Campus', choices=CAMPUS_CHOICES, validators=[DataRequired()])
    term = SelectField(label='Term', choices=TERM_CHOICES, validators=[DataRequired()])
    level = SelectField(label='Level', choices=LEVEL_CHOICES, validators=[DataRequired()])
    subject = TextField(label='Subject')
    course_number = TextField(label='Course Number')
    compare = SelectField(label='Course Number', choices=COMPARE_CHOICES)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        found = False
        json_file = '/majors.json'
        initial_validation = super(SearchForm, self).validate()
        if self.course_number.data:
            if self.compare.data == '':
                self.compare.errors.append('Please enter a comparison')
                return False

        if str(self.campus.data) == 'umnmo':
            json_file = '/morris.json'
        elif str(self.campus.data) == 'umncr':
            json_file = '/crookston.json'
        elif str(self.campus.data) == 'umndl':
            json_file = '/duluth.json'

        json_url = os.path.realpath(os.path.dirname(__file__)) + json_file
        f = open(json_url,'r')

        json_data = json.loads(f.read())
        subject = self.subject.data.upper()
        for key, value in json_data.iteritems():
            if subject == key:
                found = True
        if not found:
            self.subject.errors.append('Please enter a valid course subject')
            return False
        return True

