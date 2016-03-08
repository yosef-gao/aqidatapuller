import sae
import urllib
import json
import os
from pull_data import write_aqi_to_file
from sae.storage import Bucket

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    url = write_aqi_to_file('hangzhou')
    start_response(status, response_headers)
    return [url]

application = sae.create_wsgi_app(app)
