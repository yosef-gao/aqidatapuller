import sae
import urllib
import json
import os
from sae.storage import Bucket
#from sae.ext.storage import monkey

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    #monkey.patch_all()
    #create a instance of Bucket
    bucket = Bucket('aqi')
    # create the bucket
    #bucket.put()

    url = "http://aqicn.org/aqicn/json/android/hangzhou/json" 
    data = urllib.urlopen(url).read()
    aqi_json = json.loads(data)
    bucket.put_object('1.txt', data)
    path = bucket.generate_url('1.txt')
    start_response(status, response_headers)
    return [path]

application = sae.create_wsgi_app(app)
