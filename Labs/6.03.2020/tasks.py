from http.server import HTTPServer,CGIHTTPRequestHandler

server_address = ("",8000)

h = HTTPServer(server_address,CGIHTTPRequestHandler)

h.serve_forever()