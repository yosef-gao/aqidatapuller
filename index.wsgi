import sae
import urllib
import json

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    url = "http://aqicn.org/aqicn/json/android/hangzhou/json" 
    data = urllib.urlopen(url).read()
    aqi_json = json.loads(data)
    start_response(status, response_headers)
    return [aqi_json['aqi'].__str__()]

application = sae.create_wsgi_app(app)
