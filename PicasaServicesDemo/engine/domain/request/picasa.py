'''
Created on 15-Oct-2013

@author: sunitav
'''
from picasaengine.domain.base_domain import BaseMarshallingDomain

class Picasa(BaseMarshallingDomain):

    def __init__(self, userName, albumId, contentType, contentName):
        self.userName = userName
        self.albumId = albumId
        self.contentType = contentType
        self.contentName = contentName


