'''
Created on 16-Oct-2013

@author: sunitav
'''

from picasaengine.clients.base_client import BaseRESTClient


class GoogleAuthClient(BaseRESTClient):

    def __init__(self, username, password, service):
        '''returns requests object'''
        super(GoogleAuthClient, self).__init__()
        self.url = "https://www.google.com/accounts/ClientLogin"
        self.service = service
        self.username = username
        self.password = password


    def picasa_auth(self):
        data = 'service=lh2&accountType=GOOGLE'
        return self.request('GET', self.url, data=data, headers=headers)
