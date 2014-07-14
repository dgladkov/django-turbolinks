django-turbolinks
===========

Installation
------------

`$ pip install django-turbolinks`

Configuration
-------------

2. Add `turbolinks.middleware.TurbolinksMiddleware` after
  `django.contrib.sessions.middleware.SessionMiddleware` to your
  `MIDDLEWARE_CLASSES` setting.
3. Add `turbolinks` to your `INSTALLED_APPS` setting.
4. Run `./manage.py collectstatic`
5. Include `/static/turbolinks/turbolinks.js` script in your base template.
