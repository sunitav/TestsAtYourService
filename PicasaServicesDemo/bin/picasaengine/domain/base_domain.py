'''
Created on 15-Oct-2013

@author: sunitav
'''
class BaseMarshallingDomain(object):

    def __init__(self, **kwargs):
        super(BaseMarshallingDomain, self).__init__(**kwargs)

    def serialize(self, format_type):
        try:
            return getattr(self, '_obj_to_%s' % format_type)()
        except Exception as e:
            print('Error occured during domain object serialization')
        return None

    @classmethod
    def deserialize(cls, serialized_str, format_type):
        ret = None
        deserialization_exception = None
        if (serialized_str is not None) and (len(serialized_str) != 0):
            try:
                ret = getattr(cls, '_%s_to_obj' % format_type)(serialized_str)

            except Exception as deserialization_exception:
                print(deserialization_exception)

        return ret

    #Serialization Functions
    def _obj_to_json(self):
        raise NotImplementedError

    def _obj_to_xml(self):
        raise NotImplementedError

    #Deserialization Functions
    @classmethod
    def _xml_to_obj(cls, serialized_str):
        raise NotImplementedError

    @classmethod
    def _json_to_obj(cls, serialized_str):
        raise NotImplementedError

    def _remove_empty_values(self, dictionary):
        '''Returns a new dictionary based on 'dictionary', minus any keys with
        values that are None
        '''
        return dict((k, v) for k, v in dictionary.iteritems() if v is not None)

    @classmethod
    def _remove_namespace(cls, doc, namespace):
        """Remove namespace in the passed document in place."""
        ns = u'{%s}' % namespace
        nsl = len(ns)
        for elem in doc.getiterator():
            for key in elem.attrib:
                if key.startswith(ns):
                    new_key = key[nsl:]
                    elem.attrib[new_key] = elem.attrib[key]
                    del elem.attrib[key]
            if elem.tag.startswith(ns):
                elem.tag = elem.tag[nsl:]

