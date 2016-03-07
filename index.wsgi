import sae
sae.add_vendor_dir("vendor")
import urllib
from bs4 import BeautifulSoup

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    url = "http://aqicn.org/city/hangzhou"
    f = urllib.urlopen(url)
    data = f.read()
    soup = BeautifulSoup(data)
    tag_pm25 = soup.select("#cur_pm25")
    start_response(status, response_headers)
    return [tag_pm25[0].string.__str__()]

application = sae.create_wsgi_app(app)
