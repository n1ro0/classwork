from werkzeug.wrappers import Request, Response
from wsgiref.simple_server import make_server
from werkzeug.routing import Map, Rule

def app1(environ, start_response):
    request = Request(environ)
    print(request.args)
    resp = Response('hello', mimetype='text/plain')
    return resp(environ, start_response)

@Request.application
def app_dec(request):
    print(request.args.getlist("a"))
    res = Response('Hello')
    res.status_code = 200
    return res

def index(req):
    return Response('index page')

def hash(req, hash):
    return Response("hash=%s" % hash)


def app(environ, start_response):
    map_rule = Map([
        Rule("/", endpoint="index"),
        Rule("/<hash>", endpoint="hash")
    ])
    views = {
        "index": index,
        "hash": hash
    }

    urls = map_rule.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except:
        start_response("404 Not Found")
        return [b'rule not found']
    resp = views[endpoint](Request(environ), **args)
    return resp(environ, start_response)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 8080, app)
