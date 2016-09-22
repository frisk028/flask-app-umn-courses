# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

import json
import os

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SearchForm(Form):
    CAMPUS_CHOICES = [('umntc', 'Twin Cities'), ('umndl', 'Duluth'),
                      ('umnro', 'Rochester'), ('umncr', 'Crookston'),
                      ('umnmo', 'Morris')]

    TERM_CHOICES = [('1165', 'Summer 2016'), ('1169', 'Fall 2016'), ('1173', 'Spring 2017')]

    COMPARE_CHOICES = [('','--choose comparison--'), ('<', 'less than'), ('<=', 'less than or equal to'),
                       ('=','equal to'), ('>=', 'greater than or equal to'),
                       ('>', 'greater than')]

    LEVEL_CHOICES = [('catalog_number<5000', 'Undergraduate Courses'), 
                     ('catalog_number>4999', 'Graduate and Professional Courses')]

    CLE_CHOICES =[('AH', 'Arts and Humanities'), ('BIOL', 'Biological Sciences'), 
                  ('CIV', 'Civic Life and Ethics'), ('DSJ', 'Diversity and Social Justice'), 
                  ('ENV', 'Environment'), ('GP', 'Global Perspectives'), ('HIS','Historical Perspectives'), 
                  ('LITR', 'Literature'), ('MATH', 'Mathmatical Thinking'), ('PHYS', 'Physical Sciences'), 
                  ('SOCS', 'Social Sciences'), ('TS', 'Technology and Society'), ('WI', 'Writing Intensive')]

    GE_CHOICES = [('BIOL SCI', 'Biological Sciences'), ('COMMUNICAT', 'Written/Oral Communications'), 
                  ('ETH/CIV RE', 'Ethic/Civil Responsibility'), ('GLOB PERSP', 'Global Perspective'), 
                  ('HI/BEH/SCC', 'History & Behavioral/Social Sciences'), ('HUMAN DIV', 'Human Diversity'),  
                  ('HUMANITIES', 'Humanities'), ('LIB ED ELC', 'Liberal Education Elective'), 
                  ('PEOPLE/ENV', 'People/Environment'), ('PHYS SCI', 'Physical Sciences'), 
                  ('MATH THINK', 'Mathematical Thinking')]

    GER_CHOICES = [('ARTP', 'Artistic Performance'), ('HUM', 'Communication, Language, Literature, and Philosophy'), 
                   ('ECR', 'Ethical & Civic Responsibility'), ('ENVT', 'People and Environment'), 
                   ('FA', 'Fine Arts'), ('FL', 'Foreign Language'), ('HIST', 'Historical Perspectives'), 
                   ('SS', 'Human Behavior, Social Processes, and Institutions'), ('HDIV', 'Human Diversity'), 
                   ('IC', 'Intellectual Community'), ('IP', 'International Perspective'), 
                   ('M/SR', 'Mathematical/Symbolic Reasoning'), ('SCI', 'Physical & Biological Sciences'), 
                   ('SCIL', 'Physical & Biological Sciences with Lab'), ('WLA', 'Writing for the Liberal Arts')]

    DLE_CHOICES = [('CDIVERSITY', 'Cultural Diversity in the US'), ('FINE ARTS', 'Fine Arts'), ('GLOBAL PER', 'Global Perspectives'), 
                   ('HUMANITIES', 'Humanities'), ('LOGIC & QR', 'Logic & Quantitative Reasoning'), ('NAT SCI', 'Natural Sciences'), 
                   ('COMM & LAN', 'Oral Communication & Languages'), ('SOC SCI', 'Social Sciences'), ('SUSTAIN', 'Sustainability'),
                   ('WRITING', 'Writing & Information Literacy')]

    campus = SelectField(label='Campus', choices=CAMPUS_CHOICES, validators=[DataRequired()])
    cle = MultiCheckboxField(label='Twin Cities/Rochester Liberal Education', choices=CLE_CHOICES)
    dle = MultiCheckboxField(label='Duluth Liberal Education', choices=DLE_CHOICES)
    ge = MultiCheckboxField(label='Crookston Liberal Education', choices=GE_CHOICES)
    ger = MultiCheckboxField(label='Morris Liberal Education', choices=GER_CHOICES)
    term = SelectField(label='Term', choices=TERM_CHOICES, validators=[DataRequired()], default='1159')
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
        if subject: # make sure to only validate subject if something was entered.
            for key, value in json_data.iteritems():
                if subject == key:
                    found = True
            if not found:
                self.subject.errors.append('Please enter a valid course subject')
                return False
        return True

