import urllib2
import json

class DatePuller(object):
    URL = 'http://aqicn.org/aqicn/json/android/%s/json'
    TRYTIMES = 5

    def pull_data(self, site):
        url_with_site = DatePuller.URL % site
        # try 5 ti
        for i in range(DatePuller.TRYTIMES):
            try:
                data = urllib2.urlopen(url_with_site, timeout=3).read()
            except Exception, e:
                print 'pull_data() error %s' % (url_with_site)
            else:
                break

        aqi_json = json.loads(data)
        if aqi_json.has_key('aqi'):
            return aqi_json['aqi']
        else:
            return -1
