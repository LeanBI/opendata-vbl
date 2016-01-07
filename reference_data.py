import xml.etree.ElementTree as ET
import urllib
from os import environ

class reference_data:
    def __init__(self):
        self.elements=[]
        self.url=environ.get("URL_DATA_REFERENCE","http://www.oev.ch:8080/ref")
        self.get_data()

    def get_data(self):
        response=urllib.urlopen(self.url)
        self.xml=response.read()


    def get_elements(self,element="haltestelle"):
        self.elements=[]
        t = ET.fromstring(self.xml)
        for h in t.iter(element):
            self.elements.append(h.attrib)
        return self.elements

    def get_attrib(self,attrib="id"):
        if len(self.elements)==0:
            self.get_elements()

        attrib_list=[]
        for a in self.elements:
            attrib_list.append(a[attrib])
        return attrib_list




if __name__ == '__main__':
    print reference_data().get_attrib()