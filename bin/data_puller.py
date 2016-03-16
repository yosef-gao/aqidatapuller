import urllib2
import json
import socket
import re

class DataPuller(object):
    # URL = 'http://aqicn.org/aqicn/json/android/%s/json'
    URL = 'http://aqicn.org/map/world'
    TRYTIMES = 10

    def __init__(self):
        data = None
        for i in range(DataPuller.TRYTIMES):
            try:
                file = urllib2.urlopen(DataPuller.URL, timeout=3)
                if file:
                    data = file.read()
            except urllib2.URLError, e:
                print 'Error in DatePuller reason:%s' % (e.reason)
            except Exception, e:
                print 'Error in DatePuller %s' % e.args[0]
            else:
                break

        if data:
            fullMapJsonString = re.search("(?<=mapInitWithData\()\[.*\](?=\))", data)
            cities = None
            if fullMapJsonString:
                self.cities = json.loads(fullMapJsonString.group(0))

    def pull_data(self, site_id):
        for city in self.cities:
            if city['x'] == site_id:
                return city['aqi']
