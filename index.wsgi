import sae
from csv_generator import CSVGenerator
from mysql_db import Mysql

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    
    # query data from mdb
    site = 'beijing'
    mysql = Mysql()
    results = mysql.query_data(site) 
    csv_generator = CSVGenerator(site)
    for line in results:
        csv_generator.write_line(line[0], line[1])
    file_url = csv_generator.generate_csv_file()
    start_response(status, response_headers)
    return [file_url]

application = sae.create_wsgi_app(app)
