#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 17, 2015

@author: Sébastien Brennion
'''
import urllib
from   os import environ
import logging
from object_storage import object_storage
from reference_data import reference_data
import requests
import datetime

class transaction_data():
    def __init__(self,**kwargs):
        self.base_url=environ.get("URL_DATA_TRANSACTION","http://dfi.oev-live.ch:8080/dfirequest")
        self.storage=object_storage()



    def get_data(self):
        self.reference_data=reference_data()
        requested_date=datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime("%Y-%m-%d")
        for halt in self.reference_data.get_elements():
            h=halt["id"]
            if h == "null" :
                logging.warning("haltestelle=%s has no id, and can't be retrieved" % halt["name"])
            else :
                r = requests.get(self.base_url, params={'haltestelleid':h,"datum":requested_date })
                logging.debug(r.url)
                self.store(r.text,tstamp=requested_date, id=h)


    def store(self,myString,**kwargs):
        fileName="%s%s/%s.xml" % (environ["S3_KEY"],kwargs["tstamp"],kwargs["id"])
        logging.debug("storing in file %s" % fileName)
        self.storage.put(environ["S3_BUCKET"],fileName,myString)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s  %(levelname)7s %(lineno)s %(name)s  - %(message)s',
                        level=getattr(logging,environ.get("LOG_LEVEL","INFO"))
                        )
    transaction_data().get_data()

    
    
    
    
    
    
    
    