'''
Created on 16-Oct-2013

@author: sunitav
'''
from picasaengine.domain.base_domain import BaseMarshallingDomain
import json
import xml.etree.ElementTree as ET

class Feed(BaseMarshallingDomain):

    def __init__(self, **kwargs):
        super(Feed, self).__init__(**kwargs)
        for keys, values in kwargs.items():
            setattr(self, keys, values)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        '''Returns an instance of a Flavor based on the xml serialized_str
        passed in.'''
        element = ET.fromstring(serialized_str)
        cls.strip_namespace(element)
        if element.tag == 'feed':
            feed = cls._xml_ele_to_obj(element)
            return feed

    @classmethod
    def _xml_ele_to_obj(cls, element):
        feed_dict = element.attrib
        feed = Feed(**feed_dict)
        if element.find('entry') is not None:
            feed.entries = Entries._xml_ele_to_obj(element)

        return feed

    @classmethod
    def strip_namespace(cls, element):
        cls._remove_namespace(element, 'http://www.w3.org/2005/Atom')
        cls._remove_namespace(element, 'http://a9.com/-/spec/opensearchrss/1.0/')
        cls._remove_namespace(element, 'http://www.w3.org/2003/01/geo/wgs84_pos#')
        cls._remove_namespace(element, 'http://www.opengis.net/gml')
        cls._remove_namespace(element, 'http://www.georss.org/georss')
        cls._remove_namespace(element, 'http://www.pheed.com/pheed/')
        cls._remove_namespace(element, 'http://search.yahoo.com/mrss/')
        cls._remove_namespace(element, 'http://schemas.google.com/gdata/batch')
        cls._remove_namespace(element, 'http://schemas.google.com/photos/2007')


class Entries(BaseMarshallingDomain):

    def __init__(cls, entries_list):
        super(Entry, self).__init__()
        self.entries = {}
        if entries_list is not None:
            for entry in entries_list:
                self.entries[link['rel']] = link['href']
            for key_name in self.entries:
                setattr(self, key_name, self.entries[key_name])
            if hasattr(self.entries, 'gphoto:id'):
                setattr(self.entries, 'gphoto_id', self.entries.pop('gphoto:id'))

    @classmethod
    def _xml_ele_to_obj(cls, element):
        '''Helper method to turn ElementTree instance to Entries instance.'''
        entries = []
        if element.findall('entry'):
            for entry in element.findall('entry'):
                entries.append(entry.attrib)
        return Entries(entries)



