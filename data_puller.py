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
                data = urllib2.urlopen(url_with_site).read()
            except urllib2.HTTPError, e:
                print 'pull_data() %d: %s' % (e.args[0], e.args[1])
            except urllib2.URLError, e:
                print 'pull_data() %d: %s' % (e.args[0], e.args[1])
            else:
                break

        aqi_json = json.loads(data)
        return aqi_json['aqi']
