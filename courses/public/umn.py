# -*- coding: utf-8 -*-

import urllib, json

def get_courses(campus,term,subject,course_number=None,compare=None):
	url = 'http://courses.umn.edu/campuses/%s/terms/%s/courses.json?q=subject_id=%s' % (campus, term, subject)
	if course_number:
		url += ',catalog_number%s%s' % (compare, course_number)
	response = urllib.urlopen(url);
	data = json.loads(response.read())
	return data