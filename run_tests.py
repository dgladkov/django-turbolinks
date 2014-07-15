#!/usr/bin/env python
from __future__ import unicode_literals
import os
import django
from django.conf import settings
from django.conf.urls import patterns
from django.http import HttpResponse, HttpResponseRedirect


# Setup
if not settings.configured:
    settings.configure(
        ROOT_URLCONF='run_tests',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite3'),
            }
        },
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'turbolinks.middleware.TurbolinksMiddleware'
        ),
        INSTALLED_APPS=(
            'django.contrib.sessions',
            'turbolinks',
        ),
    )
    # Django >=1.7 compatibility
    if hasattr(django, 'setup'):
        django.setup()

# URLConf
urlpatterns = patterns('run_tests',
    (r'^$', 'index'),
    (r'^page/$', 'page'),
    (r'^redirect/$', 'redirect'),
    (r'^x-redirect/$', 'x_redirect'),
)


# Views
def index(request):
    return HttpResponse(request.META.get('HTTP_REFERER', ''))


def page(request):
    return HttpResponse('page')


def redirect(request):
    return HttpResponseRedirect('/page/')


def x_redirect(request):
    return HttpResponseRedirect('http://example.com')


# Tests
from django.test import TestCase


class MainTestCase(TestCase):

    def test_home(self):
        response = self.client.get('/', HTTP_X_XHR_REFERER='/page/')
        self.assertEqual(response.content, b'/page/')
        self.assertEqual(response.cookies.get('request_method').value, 'GET')

    def test_redirect(self):
        response = self.client.get('/redirect/', HTTP_X_XHR_REFERER='/page/')
        self.assertEqual(
            self.client.session.get('_turbolinks_redirect_to'),
            '/page/',
        )
        self.assertNotIn('X-XHR-Redirected-To', response)

        response = self.client.get('/page/', HTTP_X_XHR_REFERER='/redirect/')
        self.assertNotIn('_turbolinks_redirect_to', self.client.session)
        self.assertIn('X-XHR-Redirected-To', response)

    def test_cookie(self):
        self.client.cookies['request_method'] = 'GET'
        response = self.client.get('/', HTTP_X_XHR_REFERER='/page/')
        self.assertFalse(response.cookies)

    def test_x_redirect(self):
        response = self.client.get('/x-redirect/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/x-redirect/', HTTP_X_XHR_REFERER='/page/')
        self.assertEqual(response.status_code, 403)

        # origin and redirect are exactly the same
        response = self.client.get(
            '/x-redirect/',
            HTTP_X_XHR_REFERER='http://example.com/'
        )
        self.assertEqual(response.status_code, 302)

        # port differs
        response = self.client.get(
            '/x-redirect/',
            HTTP_X_XHR_REFERER='http://example.com:8000/'
        )
        self.assertEqual(response.status_code, 403)

        # same domain, different URI
        response = self.client.get(
            '/x-redirect/',
            HTTP_X_XHR_REFERER='http://example.com/example/'
        )
        self.assertEqual(response.status_code, 302)


def main():
    from django.core import management
    management.call_command(
        'test',
        'run_tests',
    )

if __name__ == '__main__':
    main()
