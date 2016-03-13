from data_puller import DatePuller
from sae.storage import Bucket
from mysql_db import Mysql
from csv_generator import CSVGenerator

def cron_task():
    BUCKET = 'citylist'
    # read citylist
    bucket = Bucket(BUCKET)
    citylist_content = bucket.get_object_contents('capital_cities_has_data.txt')
    citylist = citylist_content.split()
    # datepuller
    date_puller = DatePuller()
    # mysql
    mysql = Mysql()

    for city in citylist:
        value = date_puller.pull_data(city)
        if value == -1:
            continue
        else:
            mysql.insert_data(city, value)

    # done!

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
    citylist_content = bucket.get_object_contents('capital_cities_has_data.txt')
    citylist = citylist_content.split()

    values.append('<ul>')
    for city in citylist:
        line = '''<li><a href="%s/%s">%s</li>''' % ('http://aqidatapuller.applinzi.com', city, city)
        values.append(line)
    values.append('</ul>')
    return ''.join(values)