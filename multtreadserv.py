import socketserver


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass