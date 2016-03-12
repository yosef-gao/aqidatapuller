import sae
sae.add_vendor_dir('vendor')

from bottle import Bottle, run
from task import cron_task, generate_csv_url, generate_city_list
from csv_generator import CSVGenerator

app = Bottle()

@app.route('/')
def hello():
    list = generate_city_list()
    print list
    return "<br/><br/>Welcome! Here is the city list:<br/> %s" % list

@app.route('/task.py')
def task():
    cron_task()
    return "succeed"

@app.route('/<site>')
def site_url(site):
    url_result = generate_csv_url(site)
    if url_result[0] == True:
        return ''' <br/><br/>Welcome!<br/>Get %s aqi file from <a href="%s">%s</a> ''' % (site, url_result[1], site)
    else:
        return ''' <br/><br/>Welcome!<br/>%s has no aqi data, visit <a href="http://aqicn.org">aqicn.org</a> for more information ''' % (site)


application = sae.create_wsgi_app(app)
