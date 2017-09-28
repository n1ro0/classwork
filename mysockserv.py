import socketserver
import multtreadserv


class MyHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print(self.request, self.client_address)
        #data = self.request.recv(1024)
        data = self.rfile.readLine()
        #self.request.sendall(data.upper())
        self.wfile.write(data.upper())

if __name__ == "__main__":
    server = multtreadserv.Server(('localhost', 50001), MyHandler)
    server.serve_forever()