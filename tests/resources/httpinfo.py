from argparse import ArgumentParser
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import sys

class EchoRequestInfo(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write('{}\n'.format(self.requestline).encode())
        self.wfile.write('{}\n'.format(self.headers).encode())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('port', type=int)
    parser.add_argument('--keyfile')
    parser.add_argument('--certfile')
    args = parser.parse_args()
    server_address = ('', args.port)
    httpd = HTTPServer(server_address, EchoRequestInfo)
    if args.keyfile or args.certfile:
        httpd.socket = ssl.wrap_socket(
            httpd.socket, server_side=True,
            certfile=args.certfile, keyfile=args.keyfile)
    httpd.serve_forever()
