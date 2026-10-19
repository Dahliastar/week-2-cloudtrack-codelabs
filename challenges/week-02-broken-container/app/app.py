from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"It finally works!\n")


HTTPServer(("127.0.0.1", 5000), Handler).serve_forever()
