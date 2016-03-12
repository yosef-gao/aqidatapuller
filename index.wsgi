import sae

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    
    return ["Welcome"]

application = sae.create_wsgi_app(app)
