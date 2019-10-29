# coding: utf-8
from django.http import HttpResponse, HttpResponseForbidden
from django.utils.six.moves.urllib.parse import urlparse


def same_origin(current_uri, redirect_uri):
    a = urlparse(current_uri)
    if not a.scheme:
        return True
    b = urlparse(redirect_uri)
    return (a.scheme, a.hostname, a.port) == (b.scheme, b.hostname, b.port)


class TurbolinksMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # This header is either set by TurboLinks or
        # our turbolink_form_submit ajax submission helper
        tl_referrer = request.META.get('HTTP_TURBOLINKS_REFERRER')
        if not tl_referrer:
            # turbolinks not enabled
            return response

        if response.has_header('Location'):
            location = response['Location']
            request.session['_turbolinks_redirect_to'] = location

            # cross domain blocker
            if not same_origin(location, tl_referrer):
                return HttpResponseForbidden()

            # To properly handle redirects in AJAX-initiated
            # POST/PUT/... requests. Conformly to
            # https://github.com/turbolinks/turbolinks#redirecting-after-a-form-submission
            if request.method != 'GET':
                script = f'Turbolinks.clearCache(); Turbolinks.visit("{location}");'
                return HttpResponse(
                    script.encode('utf-8'),
                    content_type='text/javascript',
                    status=200
                )
        else:
            loc = request.session.pop('_turbolinks_redirect_to', None)
            if loc:
                response['Turbolinks-Location'] = loc

        return response
