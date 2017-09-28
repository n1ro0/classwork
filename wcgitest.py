from wsgiref.simple_server import make_server


# Web Server Gateway Interface
def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [('%s=%s\n'% (k, v)).encode("UTF-8") for k, v in environ.items()]

httpserv = make_server("localhost", 8080, app)
httpserv.serve_forever()
