import falcon, json
data = ["messege","Hello"]

class Resource:
    def on_get(self, req, resp):
        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if req.content_length:
            req_data = json.loads(req.stream.read().decode("UTF-8"))
            data.append(req_data)
        resp.status = falcon.HTTP_201

app = application = falcon.API()
app.add_route('/', Resource())

