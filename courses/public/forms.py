# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import DataRequired, Required

from courses.user.models import User

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append('Unknown username')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        if not self.user.active:
            self.username.errors.append('User not activated')
            return False
        return True

class SearchForm(Form):
    CAMPUS_CHOICES = [('umntc', 'Twin Cities'), ('umndl', 'Duluth'),
                      ('umnro', 'Rochester'), ('umncr', 'Crookston'),
                      ('umnmo', 'Morris')]

    TERM_CHOICES = [('1155', 'Summer 2015'), ('1159', 'Fall 2015'), ('1163', 'Spring 2016')]

    COMPARE_CHOICES = [('',''), ('<', 'less than'), ('<=', 'less than or equal to'),
                       ('=','equal to'), ('>=', 'greater than or equal to'),
                       ('>', 'greater than')]

    campus = SelectField(label='Campus', choices=CAMPUS_CHOICES, validators=[DataRequired()])
    term = SelectField(label='Term', choices=TERM_CHOICES, validators=[DataRequired()])
    subject = TextField(label='Subject', validators=[DataRequired()])
    course_number = TextField(label='Course Number')
    compare = SelectField(label='Course Number', choices=COMPARE_CHOICES)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(SearchForm, self).validate()
        if self.course_number:
            if self.compare.data == '':
                self.compare.errors.append('Please enter a comparison')
                return False
        return True

