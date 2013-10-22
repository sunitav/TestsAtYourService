'''
@summary: Common classes, base class types, enumerated types, etc...
          that can belong to *any* product's automated tests
@see: http://docs.python-requests.org/en/latest/api/#requests.Response
'''
import requests
from time import time


class RestConnector(object):
    '''Class re-implementation of the Reqeusts library api with verbose logging
    Removes a lot of the assumptions that the Requests library makes in api.py
    Supports response-code based exception injection.
    '''

    def __init__(self):
        super(RestConnector, self).__init__()

    def request(self, method, url, **kwargs):
        ''' Performs <method> HTTP request to <url>  using the requests lib'''
        return requests.request(method, url, **kwargs)

    def put(self, url, **kwargs):
        ''' HTTP PUT request '''
        return self.request('PUT', url, **kwargs)

    def copy(self, url, **kwargs):
        ''' HTTP COPY request '''
        return self.request('COPY', url, **kwargs)

    def post(self, url, data=None, **kwargs):
        ''' HTTP POST request '''
        return self.request('POST', url, data=data, **kwargs)

    def get(self, url, **kwargs):
        ''' HTTP GET request '''
        return self.request('GET', url, **kwargs)

    def head(self, url, **kwargs):
        ''' HTTP HEAD request '''
        return self.request('HEAD', url, **kwargs)

    def delete(self, url, **kwargs):
        ''' HTTP DELETE request '''
        return self.request('DELETE', url, **kwargs)

    def options(self, url, **kwargs):
        ''' HTTP OPTIONS request '''
        return self.request('OPTIONS', url, **kwargs)

    def patch(self, url, **kwargs):
        ''' HTTP PATCH request '''
        return self.request('PATCH', url, **kwargs)

    @classmethod
    def add_exception_handler(cls, handler):
        '''
        @summary: Adds a specific L{ExceptionHandler} to the rest connector
        @warning: SHOULD ONLY BE CALLED FROM A PROVIDER THROUGH A TEST FIXTURE
        '''
        cls._exception_handlers.append(handler)

    @classmethod
    def delete_exception_handler(cls, handler):
        '''
        @summary: Removes a specific L{ExceptionHandler} to the rest connector
        @warning: SHOULD ONLY BE CALLED FROM A PROVIDER THROUGH A TEST FIXTURE
        '''
        if handler in cls._exception_handlers:
            cls._exception_handlers.remove(handler)
