import sae
from bottle import Bottle, run
from task import cron_task

app = Bottle()

@app.route('/')
def hello():
    return "Welcome"

@app.route('/task.py')
def task():
    cron_task()
    return "succeed"

application = sae.create_wsgi_app(app)
