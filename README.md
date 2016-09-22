UMN Courses Listing
===============================

A flask app to display and search for UMN courses


Quickstart
----------


Then run the following commands to bootstrap your environment.

    git clone https://github.com/frisk028/flask-app-umn-courses
    pip install virtualenv
    virtualenv courses
    source courses/bin/activate
    cd flask-app-umn-courses
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen.


Deployment
----------

In your production environment, make sure the ``COURSES_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``.


Running Tests
-------------

To run all tests, run ::

    python manage.py test
