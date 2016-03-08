import urllib
import json
import time
from sae.storage import Bucket

ISOTIMEFORMAT='%Y/%m/%d %X'
DATETIMEFORMAT = '%Y_%m_%d'
TITLE_STR = 'Site,Parameter,Date(LST),Year,Month,Day,Hour,Value,Unit,Duration\r\n'
WRITE_STR = '%s,PM2.5,%s,%d,%d,%d,%d,%d,ug/m3,%d\r\n'
url = 'http://aqicn.org/aqicn/json/android/%s/json'
BUCKET_NAME = 'aqi'
DURATION = 1

def get_aqi(city):
    url_with_city = url % city
    data = urllib.urlopen(url_with_city).read()
    aqi_json = json.loads(data)
    return aqi_json['aqi']

def write_aqi_to_file(city):
    bucket = Bucket(BUCKET_NAME)
    # get current time
    time_str = time.strftime(ISOTIMEFORMAT, time.localtime())
    date_str = time.strftime(DATETIMEFORMAT, time.localtime())
    time_s = time.localtime()
    #if is_file_in_bucket(date_str + '%s' % '.csv'):
    #    return 'yes'
    #else:
    #    return 'no'
    # create csv file
    filename = date_str + '%s' % '.csv'
    value = get_aqi(city)
    str_list = []
    if not is_file_in_bucket(filename):
        str_list.append('Site,Parameter,Date(LST),Year,Month,Day,Hour,Value,Unit,Duration\r\n')
    str_list.append(WRITE_STR % (city, time_str, time_s.tm_year, time_s.tm_mon, time_s.tm_mday, time_s.tm_hour, value, DURATION))
    bucket.put_object(filename, ''.join(str_list))
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
