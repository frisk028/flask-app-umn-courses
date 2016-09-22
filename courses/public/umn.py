# -*- coding: utf-8 -*-
import urllib, json

cle = { 'HIS':'Historical Perspectives', 'WI': 'Writing Intensive', 
        'BIOL': 'Biological Sciences', 'PHYS': 'Physical Sciences',
        'GP': 'Global Perspective', 'LITR': 'Literature', 'ENV': 'Environment',
        'DSJ': 'Diversity and Social Justice', 'CIV': 'Civic Life and Ethics',
        'MATH': 'Mathmatical Thinking', 'AH': 'Arts and Humanities',
        'TS': 'Technology and Society', 'SOCS': 'Social Sciences'};

ge = {'HUMANITIES': 'Humanities', 'BIOL SCI': 'Biological Sciences', 
      'PEOPLE/ENV': 'People/Environment', 'PHYS SCI': 'Physical Sciences', 
      'HUMAN DIV': 'Human Diversity', 'COMMUNICAT': 'Written/Oral Communications', 
      'HI/BEH/SCC': 'History & Behavioral/Social Sciences', 
      'ETH/CIV RE': 'Ethic/Civil Responsibility', 'GLOB PERSP': 'Global Perspective',
      'MATH THINK': 'Mathematical Thinking', 'LIB ED ELC': 'Liberal Education Elective'}

ger = {'ARTP':'Artistic Performance', 'HUM': 'Communication, Language, Literature, and Philosophy', 
       'ECR':'Ethical & Civic Responsibility', 'FL': 'Foreign Language', 'ENVT': 'People and Environment',
       'SS': 'Human Behavior, Social Processes, and Institutions', 'FA': 'Fine Arts',
       'HIST': 'Historical Perspectives', 'SCIL': 'Physical & Biological Sciences with Lab',
       'SCI': 'Physical & Biological Sciences', 'HDIV': 'Human Diversity', 'IC': 'Intellectual Community', 
       'IP': 'International Perspective', 'M/SR': 'Mathematical/Symbolic Reasoning',
       'WLA': 'Writing for the Liberal Arts'}

dle = {'CDIVERSITY': 'Cultural Diversity in the US', 'FINE ARTS': 'Fine Arts', 'GLOBAL PER': 'Global Perspectives', 
       'HUMANITIES': 'Humanities', 'LOGIC & QR': 'Logic & Quantitative Reasoning', 'NAT SCI': 'Natural Sciences', 
       'COMM & LAN': 'Oral Communication & Languages', 'SOC SCI': 'Social Sciences', 'SUSTAIN': 'Sustainability',
       'WRITING': 'Writing & Information Literacy'}

other = {'TOPICS': 'Topics Course', '08': 'Classroom', 'HON': 'Honors', '13': 'Partially Online', '12': 'Primarily Online',
          '06': 'Independent Study', 'THESIS': 'Thesis Course', '01': 'Completely Online',
          'ONLINE': 'Online Course', '02': 'Computer Based'};

class Course(object):
    def __init__(self, subject='', number='', description='', repeat_limit=1, 
            attributes=[], lib_ed=[], credits_minimum='', credits_maximum='', 
            grading_basis='', sections=[], title='', frequency=''):
        self.subject = subject
        self.number = number
        self.description = description
        self.repeat_limit = repeat_limit
        self.lib_ed = lib_ed
        self.attributes = attributes
        self.credits_minimum = credits_minimum
        self.credits_maximum = credits_maximum
        self.grading_basis = grading_basis
        self.sections = sections
        self.title = title
        self.frequency = frequency

class Section(object):
    def __init__(self, number='', component='', location='', bank='', mode='', 
            instructor=[], start_time='', end_time='', days=[], class_number=''):
        self.number = number
        self.component = component
        self.location = location
        self.bank = bank
        self.mode = mode
        self.instructor = instructor
        self.start_time = start_time
        self.end_time = end_time
        self.days = days
        self.class_number = class_number

    def __cmp__(self,other):
      return cmp(int(self.number), int(other.number))

class CourseSearch(object):
    def __init__(self, url=''):
        self.url = url

    def _data(self):
        response = urllib.urlopen(self.url)
        data = json.loads(response.read())
        return data

    def get_object_list(self):
        results = []
        le = cle
        data = self._data()
        campus = data['campus']['campus_id']
        if campus == "UMNCR":
          le = ge
        elif campus == "UMNMO":
          le = ger
        elif campus == "UMNDL":
          le = dle
        courses = data['courses']
        for course in courses:
            """
            EXAMPLE OBJECT 
            {
               type: 'course',
               course_id: '024564',
               id: 5546842,
               catalog_number: '1000',
               description: 'Fundamental concepts in ....... ',
               title: 'Fundamental Econ',
               repeatable: 'N',
               repeat_limit: '1',
               units_repeat_limit: '4',
               offer_frequency: 'Every Fall',
               credits_minimum: '4',
               credits_maximum: '4',
               grading_basis: {
                  type: 'grading_basis',
                  grading_basis_id: 'OPT',
                  id: 12900,
                  description: 'Student Option'
               },
               subject: {
                  type: 'subject',
                  subject_id: 'ECON',
                  id: 216875,
                  description: 'Economics'
               },
               equivalency: {
                  type: 'equivalency',
                  equivalency_id: '02543'
               }
               course_attributes: [
                   {
                      type: 'attribute',
                      attribute_id: 'HON',
                      id: 15424,
                      family: 'HON'
                   }
               ],
               sections: [
                   {
                      type: 'section',
                      id: 12551236,
                      class_number: '20005',
                      number: '001',
                      component: 'LEC',
                      location: 'TCWESTBANK',
                      notes: '',
                      instruction_mode: {
                          type: 'instruction_mode',
                          instruction_mode_id: 'P',
                          id: 12702,
                          description: 'In Person Term Based'
                      },
                      instructors: [
                          {
                              type: 'instructor',
                              name: 'Michael Bunt',
                              email: 'bunt@umn.edu',
                              role: 'PI'
                          },
                          {
                              type: 'instructor',
                              name: null,
                              email: null,
                              role: 'TA'
                          }
                      ],
                      meeting_patterns: [
                          {
                              type: 'meeting_pattern',
                              start_time: '18:50',
                              end_time: '20:40',
                              start_date: '2015-09-08',
                              end_date: '2015-12-16',
                              location: {
                                  type: 'location',
                                  location_id: 'HH/EC21597,
                                  id: 158452,
                                  description: 'Heller Hall 597'
                              },
                              days: [
                                  {
                                      type: 'day',
                                      name: 'Monday',
                                      abbreviation: 'm'
                                  }
                              ]
                          }
                      ],
                      combined_sections: []
                   }
               ]
            }
            """
            sections=[]
            attributes=[]
            lib_ed=[]
            for section in course['sections']:
                instructors = []
                days = []
                for instructor in section['instructors']:
                    if instructor['role'] == 'PI':
                        instructors.append(instructor['name'])
                pattern = section['meeting_patterns'][0]
                try:
                    location = pattern['location']['description']
                except:
                    location=''
                start_time = pattern['start_time']
                end_time = pattern['end_time']
                for day in pattern['days']:
                    days.append(day['abbreviation'])
                sections.append(
                    Section(
                        number=section['number'],
                        component=section['component'],
                        location=location,
                        bank=section['location'],
                        mode=section['instruction_mode']['description'],
                        instructor=instructors,
                        start_time=start_time,
                        end_time=end_time,
                        days=days,
                        class_number=section['class_number']))
            for attribute in course['course_attributes']:
                a = le.get(attribute['attribute_id'])
                if not a:
                  a = other.get(attribute['attribute_id'], attribute['attribute_id'])
                  attributes.append(a)
                else:
                  lib_ed.append(a)
                  
            sections.sort(key = lambda s: s.number)
            results.append(
                Course(
                    subject=course['subject']['subject_id'],
                    number=course['catalog_number'],
                    description=course['description'],
                    repeat_limit=course['units_repeat_limit'],
                    attributes=attributes,
                    lib_ed=lib_ed,
                    credits_minimum=course['credits_minimum'],
                    credits_maximum=course['credits_maximum'],
                    grading_basis=course['grading_basis']['description'],
                    sections=sections,
                    title=course['title'],
                    frequency=course['offer_frequency']))
        return results



def get_courses(campus, level, subject,course_number=None,compare=None, le=[]):
    url = 'http://courses.umn.edu/campuses/%s/terms/1169/courses.json?q=%s' % (campus, level)
    if subject:
        url += ',subject_id=%s' % subject
    if course_number:
  		url += ',catalog_number%s%s' % (compare, course_number)
    if le != []:
      f = le.pop()
      url += ',course_attribute_id=%s' % f
      for l in le:
        url += '|%s' % l

    data = CourseSearch(url).get_object_list()

    if len(data) > 500:
        data = None
    
    return data


def get_classes(campus, term, level, subject,course_number=None,compare=None, le=[]):
    url = 'http://courses.umn.edu/campuses/%s/terms/%s/classes.json?q=%s' % (campus, term, level)
    if subject:
        url += ',subject_id=%s' % subject
    if course_number:
        url += ',catalog_number%s%s' % (compare, course_number)
    
    data = CourseSearch(url).get_object_list()

    if len(data) > 500:
        data = None
    
    return data