from data_puller import DatePuller
from sae.storage import Bucket
from mysql_db import Mysql

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
        mysql.insert_data(city, value)

    # done!
