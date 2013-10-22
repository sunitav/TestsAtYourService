'''
Created on 15-Oct-2013

@author: sunitav

'''
from picasaengine.common.rest import RestConnector

class BaseRESTClient(RestConnector):
    '''
        Allows clients to inherit all requests-defined RESTfull verbs.
        This version inherits from both the client and the connector, but acts
        like a Client first in the mro

        requests documentation:
        http://docs.python-requests.org/en/latest/api/#configurations
    '''

    def __init__(self):
        super(BaseRESTClient, self).__init__()
        self.default_headers = {}

    def request(self, method, url, headers=None, params=None, data=None,
                requestslib_kwargs=None):

        #set requestslib_kwargs to an empty dict if None
        requestslib_kwargs = requestslib_kwargs if\
                                     requestslib_kwargs is not None else {}

        #Set defaults
        params = params if params is not None else {}
        headers = self.default_headers
        verify = False

        #Override url and method if present in requestslib_kwargs
        if 'url' in requestslib_kwargs.keys():
            url = requestslib_kwargs.get('url', None) or url
            del requestslib_kwargs['url']

        if 'method' in requestslib_kwargs.keys():
            method = requestslib_kwargs.get('method', None) or method
            del requestslib_kwargs['method']

        #Delete key:value pairs from requestslib_kwargs if the value=None
        for key, _ in requestslib_kwargs.items():
            if requestslib_kwargs[key] is None:
                del requestslib_kwargs[key]

        #Assign final values to requestslib_kwargs, but prevent this method's
        #kwarg's values from overwriting requestslib_kwargs values.
        requestslib_kwargs = dict({'headers': headers,
                                   'params': params,
                                   'verify': verify,
                                   'data': data},
                                   **requestslib_kwargs)

        #Return final requests response object
        return super(BaseRESTClient, self).request(method, url,
                                                          **requestslib_kwargs)

class BaseMarshallingClient(BaseRESTClient):
    def __init__(self, serialize_format=None, deserialize_format=None):
        super(BaseMarshallingClient, self).__init__()
        self.serialize_format = serialize_format or 'xml'
        self.deserialize_format = deserialize_format or self.serialize_format

    def request(self, method, url, headers=None, params=None, data=None,
                response_entity_type=None, request_entity=None,
                requestslib_kwargs=None):

        #defaults requestslib_kwargs to a dictionary if it's None
        requestslib_kwargs = requestslib_kwargs if\
                                         requestslib_kwargs is not None else {}

        #set the 'data' paramater of the request to either what's already in
        #requestslib_kwargs, or the deserialized output of the request_entity
        if request_entity is not None:
            requestslib_kwargs = dict({'data': request_entity.serialize(
                                 self.serialize_format)}, **requestslib_kwargs)
            requestslib_kwargs = requestslib_kwargs if\
                                     requestslib_kwargs is not None else {}

        #Set defaults
        params = params if params is not None else {}
        headers = self.default_headers
        verify = False

        #Override url and method if present in requestslib_kwargs
        if 'url' in requestslib_kwargs.keys():
            url = requestslib_kwargs.get('url', None) or url
            del requestslib_kwargs['url']

        if 'method' in requestslib_kwargs.keys():
            method = requestslib_kwargs.get('method', None) or method
            del requestslib_kwargs['method']

        #Delete key:value pairs from requestslib_kwargs if the value=None
        for key, _ in requestslib_kwargs.items():
            if requestslib_kwargs[key] is None:
                del requestslib_kwargs[key]

        #Assign final values to requestslib_kwargs, but prevent this method's
        #kwarg's values from overwriting requestslib_kwargs values.
        requestslib_kwargs = dict({'headers': headers,
                                   'params': params,
                                   'verify': verify,
                                   'data': data},
                                   **requestslib_kwargs)


        #Make the actual request
        response = super(BaseMarshallingClient, self).request(method, url,
                         headers=headers, params=params, data=data,
                         requestslib_kwargs=requestslib_kwargs)

        #Append the de/serialized data object to the response
        response.request.__dict__['entity'] = None
        response.__dict__['entity'] = None

        if response.request is not None:
            response.request.__dict__['entity'] = request_entity

        if response_entity_type is not None:
            response.__dict__['entity'] = \
                    response_entity_type.deserialize(response.content,
                                                     self.deserialize_format)
        return response

