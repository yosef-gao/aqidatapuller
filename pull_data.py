import urllib2
import json
import time
from sae.storage import Bucket
from StringIO import StringIO

ISOTIMEFORMAT='%m/%d/%y %X'
DATETIMEFORMAT = '%Y_%m_%d'
TITLE_STR = 'Site,Parameter,Date(LST),Year,Month,Day,Hour,Value,Unit,Duration\r\n'
WRITE_STR = '%s,PM2.5,%s,%d,%d,%d,%d,%d,ug/m3,%d Hr\r\n'
url = 'http://aqicn.org/aqicn/json/android/%s/json'
BUCKET_NAME = 'aqi'
DURATION = 1

def get_aqi(city):
    url_with_city = url % city
    while True:
        try:
            data = urllib2.urlopen(url_with_city).read()
        except urllib2.HTTPError, e:
            print e.code
        except urllib2.URLError, e:
            print e.reason
        else:
            print 'ok'
            break

    aqi_json = json.loads(data)
    return aqi_json['aqi']

def write_aqi_to_file(city):
    bucket = Bucket(BUCKET_NAME)
    # get current time
    time_str = time.strftime(ISOTIMEFORMAT, time.localtime())
    date_str = time.strftime(DATETIMEFORMAT, time.localtime())
    time_s = time.localtime()
    string_file = StringIO()
    filename = date_str + '%s' % '.csv'
    value = get_aqi(city)
    # if there is no such file, then write the title
    if not is_file_in_bucket(filename):
        string_file.write('Site,Parameter,Date(LST),Year,Month,Day,Hour,Value,Unit,Duration\r\n')
    else: # else read from file, and append data
        data = bucket.get_object_contents(filename)
        string_file.write(data)
    string_file.write(WRITE_STR % (city, time_str, time_s.tm_year, time_s.tm_mon, time_s.tm_mday, time_s.tm_hour, value, DURATION))
    bucket.put_object(filename, string_file.getvalue())
    return bucket.generate_url(filename)

def is_file_in_bucket(filename):
    bucket = Bucket(BUCKET_NAME)
    for bucket_object in bucket.list():
        if bucket_object['name'] == filename:
            return True
    return False
    #file_obj = bucket.get_object(filename)
    #if file_obj == Null:
    #    return True
    #else:
    #    return False
