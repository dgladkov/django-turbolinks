class TurbolinksMiddleware(object):

    def process_response(self, request, response):
        response['X-XHR-Current-Location'] = request.get_full_path()
        response.set_cookie('request_method', request.method)
        return response
