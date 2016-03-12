import sae
from bottle import Bottle, run
from task.py import cron_task

app = Bottle()

@app.route('/')
def app(environ, start_response):
    return "Welcome"

@app.route('/task.py')
def task():
    cron_task()
    return "succeed"

application = sae.create_wsgi_app(app)
