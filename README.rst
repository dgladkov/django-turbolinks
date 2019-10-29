django-turbolinks-dj2 |Build Status|
================================

Drop-in turbolinks implementation for Django 2.2+.
Based on https://github.com/dgladkov/django-turbolinks.


Differences with upstream
-------------------------

* Remove Python < 3.4 support
* Remove Django < 2 support
* Rewrite middleware to support Redirects-To-Javascript transformation.


Installation
------------

``$ pip install django-turbolinks-dj2``

Configuration
-------------

1. Add ``django_turbolinks.middleware.TurbolinksMiddleware`` after
   ``django.contrib.sessions.middleware.SessionMiddleware`` to your
   ``MIDDLEWARE_CLASSES`` setting.
2. Add ``django_turbolinks`` to your ``INSTALLED_APPS`` setting.
3. Run ``./manage.py collectstatic``
4. Include Turbolinks JS from a CDN (https://cdnjs.com/libraries/turbolinks)
5. [OPTION - for Ajax form submissions] Include ``/static/django_turbolinks/turbolinks_django.js``
   script in your base template. Add `data-use-turbolinks='true'` to form tags that should
   be handled by Turbolinks. Add `<script>TurbolinksDjango.install_form_submit_handler();</script>`
   to `<head>`.

.. |Build Status| image:: https://travis-ci.org/dbarbeau/django-turbolinks-dj2.svg?branch=master
   :target: https://travis-ci.org/dbarbeau/django-turbolinks-dj2
