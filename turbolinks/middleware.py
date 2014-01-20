# coding: utf-8
"""
django_turbolinks
~~~~~~~~~~~~~~~~
some of this code copy from https://github.com/lepture/flask-turbolinks
thanks for Hsiaoming Yang <me@lepture.com> and rei <http://chloerei.com/>
"""

try:
    from urlparse import urlparse
except ImportError:
    # python 3
    from urllib.parse import urlparse

    __version__ = '0.0.1'

def same_origin(current_uri, redirect_uri):
    parsed_uri = urlparse(current_uri)
    if not parsed_uri.scheme:
        return True
    parsed_redirect = urlparse(redirect_uri)

    if parsed_uri.scheme != parsed_redirect.scheme:
        return False

    if parsed_uri.hostname != parsed_redirect.hostname:
        return False

    if parsed_uri.port != parsed_redirect.port:
        return False
    return True


class TurbolinksMiddleware(object):

    def process_response(self, request, response):
        referrer = request.META.get('HTTP_X_XHR_REFERER', None)
        if not referrer:
            # turbolinks not enabled
            return response

        method = request.COOKIES.get('request_method', None)
        if not method or method != request.method:
            response.set_cookie('request_method', request.method)
        if response.has_header('Location'):
            # this is a redirect response
            loc = response['Location']
            request.session['_turbolinks_redirect_to'] = loc
            # cross domain redirect
            if referrer and not same_origin(loc, referrer):
                response.status_code = 403
        else:
            if request.session.get('_turbolinks_redirect_to', None):
                loc = request.session.pop('_turbolinks_redirect_to')
                response['X-XHR-Redirected-To'] = loc
        return response



