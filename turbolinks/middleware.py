# coding: utf-8
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
from django.http import HttpResponseForbidden


def same_origin(current_uri, redirect_uri):
    a = urlparse(current_uri)
    if not a.scheme:
        return True
    b = urlparse(redirect_uri)
    return (a.scheme, a.hostname, a.port) == (b.scheme, b.hostname, b.port)


class TurbolinksMiddleware(object):

    def process_request(self, request):
        referrer = request.META.get('HTTP_X_XHR_REFERER')
        if referrer:
            # overwrite referrer
            request.META['HTTP_REFERER'] = referrer
        return

    def process_response(self, request, response):
        referrer = request.META.get('HTTP_X_XHR_REFERER')
        if not referrer:
            # turbolinks not enabled
            return response

        method = request.COOKIES.get('request_method')
        if not method or method != request.method:
            response.set_cookie('request_method', request.method)

        if response.has_header('Location'):
            # this is a redirect response
            loc = response['Location']
            request.session['_turbolinks_redirect_to'] = loc

            # cross domain blocker
            if referrer and not same_origin(loc, referrer):
                return HttpResponseForbidden()
        else:
            if request.session.get('_turbolinks_redirect_to'):
                loc = request.session.pop('_turbolinks_redirect_to')
                response['X-XHR-Redirected-To'] = loc
        return response
