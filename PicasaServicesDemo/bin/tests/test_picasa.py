'''
Created on 16-Oct-2013

@author: sunitav
'''

from tests.testfixtures.picasa_fixture import PicasaFixture
import sys
import time
import xml.dom.minidom

class PicasaTest(PicasaFixture):

    def test_list_albums(self):
        print("-------------------------------------------------------------")
        print("Fetching album list for user {0}\n").format(self.userName)
        response = self.picasaClient.list_albums(self.userName)
        xml_string = xml.dom.minidom.parseString(str(response))
        pretty_xml_as_string = xml_string.toprettyxml()
        print("-------------------------------------------------------------")
        print("Response {0}\n").format(pretty_xml_as_string)
        entries = response.entry
        self.assertTrue(len(entries) == 1)
        elapsed = (time.clock() - self.start)
        print("-------------------------------------------------------------")
        print("Ending Test Now")
        print("-------------------------------------------------------------")
        print("\nTime taken: {0}".format(elapsed))

if __name__ == '__main__':
    unittest.main()
