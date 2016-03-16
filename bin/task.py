from data_puller import DataPuller
from sae.storage import Bucket
from mysql_db import Mysql
from csv_generator import CSVGenerator
import json

def cron_task():
    BUCKET = 'citylist'
    # read citylist
    bucket = Bucket(BUCKET)
    citylist_content = bucket.get_object_contents('cities.json')
    cities = json.loads(citylist)
    # datepuller
    data_puller = DataPuller()
    # mysql
    mysql = Mysql()

    for city in cities:
        value = date_puller.pull_data(int(city['cid']))
        if value:
            print "insert %s: %d" % (city['city'], int(value))
            mysql.insert_data(city['city'], int(value))


def generate_csv_url(site):
    # csv generator
    csv_generator = CSVGenerator(site)
    # query data from db
    mysql = Mysql()
    results = mysql.query_data(site)
    if results == None:
        return [False, None]
    for line in results:
        csv_generator.write_line(line[0], line[1])
    return [True, csv_generator.generate_csv_file()]

def generate_city_list():
    values = []
    #read citylist
    BUCKET = 'citylist'
    # read citylist
    bucket = Bucket(BUCKET)
    citylist_content = bucket.get_object_contents('cities.json')
    citylist = citylist_content.split()

    values.append('<ul>')
    for city in citylist:
        line = '''<li><a href="%s/%s">%s</li>''' % ('http://aqidatapuller.applinzi.com', city['city'].lower(), city)
        values.append(line)
    values.append('</ul>')
    return ''.join(values)
