django-turbolinks |Build Status|
================================

Drop-in turbolinks implementation for Django

Installation
------------

    .. code-block:: console

        pip install django-turbolinks



Configuration
-------------

1. Add ``turbolinks.middleware.TurbolinksMiddleware`` after
   ``django.contrib.sessions.middleware.SessionMiddleware`` to your
   ``MIDDLEWARE_CLASSES`` in ``settings.py``.

   .. code-block:: python

        MIDDLEWARE = [
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'turbolinks.middleware.TurbolinksMiddleware',
        ...
        ]


2. Add ``turbolinks`` to your ``INSTALLED_APPS`` in ``settings.py``.

   .. code-block:: python

       INSTALLED_APPS = [
            ...
            'turbolinks',
            ...
        ]

3. Run in terminal

   .. code-block:: console

       ./manage.py collectstatic


4. Include ``/static/turbolinks/turbolinks.js`` script in your base
   template.

   .. code-block:: html

       {% load static %}

       <script src="{% static 'turbolinks/turbolinks.js' %}"></script>

   or

   .. code-block:: html

       <script src="/static/turbolinks/turbolinks.js"></script>

.. |Build Status| image:: https://travis-ci.org/dgladkov/django-turbolinks.svg?branch=master
   :target: https://travis-ci.org/dgladkov/django-turbolinks
