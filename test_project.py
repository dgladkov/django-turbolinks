#!/usr/bin/env python
from __future__ import unicode_literals

try:
    import django
except ImportError:
    django = None
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect


# Configuration
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        MIDDLEWARE_CLASSES=[
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'turbolinks.middleware.TurbolinksMiddleware'
        ],
        INSTALLED_APPS=[
            'django.contrib.sessions',
            'turbolinks',
        ],
    )
    # Django >=1.7 compatibility
    if hasattr(django, 'setup'):
        django.setup()


# URL Router
urlpatterns = []


def route(regex):
    def inner(view):
        urlpatterns.append(url(regex, view))
        return view
    return inner


# Views
@route(r'^$')
def index(request):
    return HttpResponse(request.META.get('HTTP_REFERER', ''))


@route(r'^page/$')
def page(request):
    return HttpResponse('page')


@route(r'^redirect/$')
def redirect(request):
    return HttpResponseRedirect('/page/')


@route(r'^x-redirect/$')
def x_redirect(request):
    return HttpResponseRedirect('http://example.com')


# CLI
def main():
    from django.core.management import execute_from_command_line
    execute_from_command_line()


if __name__ == '__main__':
    main()
