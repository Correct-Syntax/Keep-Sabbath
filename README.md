# Keep-Sabbath
Django app to automatically redirect users when it is the Sabbath day, with support for overriding on other Biblical Holy days.

For webmasters with e-commerce shops, etc. who would like to keep the Sabbath day holy. This app allows you to easily setup a system that will automatically* redirect visitors to a single page (explaining about the sabbath, redirect, etc.) if it is the Sabbath day. The app uses an API and the date and time of the server to figure out if it is the Sabbath, so you do not have to do it manually. However, there is an option to override it as well.

* not completed yet

Features
--------

-  Simple setup
-  Two main methods to use it
-  Automatically redirects when it is the Sabbath*
-  Support for overriding

* not completed yet

Get Started
-----------

Install
^^^^^^^

Django-Keep-Sabbath is best installed via PyPI. To install the latest version, run:

.. code:: bash

    pip install django-keep-sabbath

or Install from Github source:

.. code:: bash

    pip install git+git://github.com/Correct-Syntax/Keep-Sabbath.git

Install Requires 
----------------

-  `django`_ >=2.2
.. _django: http://djangoproject.com



Quickstart
==========

Add keep_sabbath to INSTALLED_APPS in settings.py for your project:

.. code-block::

    INSTALLED_APPS = (
        ...
        'keep_sabbath',
    )
    
Include ```keep_sabbath.urls``` inside the urlpatterns list in urls.py for your project:

.. code-block::
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        ...
        path('sabbath-redirect/', include('keep_sabbath.urls')),
        ...
    ]


Add SABBATH_REDIRECT_TEMPLATE in settings.py for your project and set it to the name of the template you want visitors to be redirected to when it is the Sabbath:

.. code-block::

    SABBATH_REDIRECT_TEMPLATE = "sabbath/redirect.html"


Add IS_SABBATH_OVERRIDE in settings.py for your project and set it to False if you do not want to overrride or True if you do (e.g: on a Holy day you will want to set this to True):

.. code-block::

    IS_SABBATH_OVERRIDE = False #or True if you want to override

In your views.py file (Method 1):

.. code-block::

    from keep_sabbath.sabbath import redirect_if_sabbath

    # Method 1 (easier, but less control)
    @redirect_if_sabbath
    def my_firstview(request):
        ...

In your views.py file (Method 2):

.. code-block::
    
    from keep_sabbath.sabbath import is_sabbath

    # Method 2 (you figure out the view logic, but more control)
    def my_secondview(request):
        ...
        if is_sabbath() == True:
          ...


Documentation
-------------

.. _English: https://


Changelogs
-------------

0.5.0
^^^^^
    
- Alpha Release


Help
----

Help is always welcome!

