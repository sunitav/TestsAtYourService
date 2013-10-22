'''
Created on 15-Oct-2013

@author: sunitav
'''

from base_client import BaseMarshallingClient
from urlparse import urlparse
from picasaengine.domain.response.picasa_response import Feed
import gdata.photos.service
import logging

class PicasaApiClient(BaseMarshallingClient):

    def __init__(self, username, password, serialize_format=None,
                 deserialize_format=None):
        super(PicasaApiClient, self).__init__(serialize_format,
                                               deserialize_format)
        gd_client = gdata.photos.service.PhotosService()
        gd_client.email = username
        gd_client.password = password
        print("-------------------------------------------------------------")
        print("Authenticating User Now")
        print("-------------------------------------------------------------")
        gd_client.ProgrammaticLogin()
        print("Received auth token: {0}").format(gd_client.current_token)
        self.client = gd_client

    def list_albums(self, user):
        albums = self.client.GetUserFeed(user=user)
        return albums
