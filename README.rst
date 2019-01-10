django-turbolinks |Build Status|
================================

Drop-in turbolinks_ implementation for Django

turbolinks version: 5.2.0 (https://github.com/turbolinks/turbolinks/releases/tag/v5.2.0)

Installation
------------

``pip install -e git+https://github.com/avelino/django-turbolinks.git#egg=django-turbolinks``

Configuration
-------------

1. Add ``turbolinks.middleware.TurbolinksMiddleware`` after
   ``django.contrib.sessions.middleware.SessionMiddleware`` to your
   ``MIDDLEWARE_CLASSES`` setting.
2. Add ``turbolinks`` to your ``INSTALLED_APPS`` setting.
3. Run ``./manage.py collectstatic``
4. Include ``/static/turbolinks/turbolinks.js`` script in your base
   template.

.. |Build Status| image:: https://travis-ci.org/dgladkov/django-turbolinks.svg?branch=master
   :target: https://travis-ci.org/dgladkov/django-turbolinks

_turbolinks: https://github.com/turbolinks/turbolinks
