# -*- coding: utf-8 -*-

import urllib, json

def get_courses(campus, level, subject,course_number=None,compare=None):
    url = 'http://courses.umn.edu/campuses/%s/terms/1159/courses.json?q=%s' % (campus, level)
    if subject:
        url += ',subject_id=%s' % subject
    if course_number:
		url += ',catalog_number%s%s' % (compare, course_number)

    response = urllib.urlopen(url);
    data = json.loads(response.read())
    
    if len(data['courses']) > 200:
	    data = None
    return data


def get_classes(campus, term, level, subject,course_number=None,compare=None):
    url = 'http://courses.umn.edu/campuses/%s/terms/%s/classes.json?q=%s' % (campus, term, level)
    if subject:
        url += ',subject_id=%s' % subject
    if course_number:
        url += ',catalog_number%s%s' % (compare, course_number)
    response = urllib.urlopen(url);
    data = json.loads(response.read())
    
    return data