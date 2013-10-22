'''
Created on 16-Oct-2013

@author: sunitav
'''

#from engine.common.auth_client import GoogleAuthClient
from picasaengine.clients.picasa_client import PicasaApiClient
from unittest import TestCase
import time
import sys


class PicasaFixture(TestCase):
    '''
    @summary: Fixture for an Picasa test.
    '''

    @classmethod
    def setUpClass(cls):
        cls.start = time.clock()
        print("\n\nStarting Test Now...")
        super(PicasaFixture, cls).setUpClass()
        '''TODO Move to config'''
        cls.userName = "rackspaceqa"
        password = "vodqapune"
        cls.url = "http://picasaweb.google.com/data"
        cls.picasaClient = PicasaApiClient(cls.userName, password,
                                          "xml",
                                          "xml")

    @classmethod
    def tearDownClass(cls):
        super(PicasaFixture, cls).tearDownClass()

