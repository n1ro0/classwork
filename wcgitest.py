from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape


# Web Server Gateway Interface
#p = path_info.split('/')
#if p[0] = 'path':
#id = p[1]
#/......    /?hash=....
def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    #start_response("301 ...", [("Location", "text/plain")])
    #return []
    qs = parse_qs(environ['QUERY_STRING'])
    #return [('%s=%s\n'% (k, v)).encode("UTF-8") for k, v in environ.items()]
    try:
        size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        size = 0
    data = environ['wsgi.input'].read(size)
    data = parse_qs(data)
    a = escape(qs.get('a', [""])[0])
    return [('%s = %s\n' % (k, v)).encode("UTF-8") for k, v in data.items()]
httpserv = make_server("localhost", 8080, app)
httpserv.serve_forever()
