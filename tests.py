from __future__ import unicode_literals

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
