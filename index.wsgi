import sae
sae.add_vendor_dir('vendor')

from bottle import Bottle, run
from task import cron_task, generate_csv_url
from csv_generator import CSVGenerator

app = Bottle()

@app.route('/')
def hello():
    return "Welcome"

@app.route('/task.py')
def task():
    cron_task()
    return "succeed"

@app.route('/<site>')
def site_url(site):
    return ''' Get %s aqi file from <a href="%s">%s</a> ''' %  (site, generate_csv_url(site), site)

application = sae.create_wsgi_app(app)
