#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import time
from tracker import *

# Port
PORT = 8000

# Set up our web handler
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# What it accepts
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
    '.jpg': 'image/jpg',
});

# Setup server as 127.0.0.1
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port", PORT

# Serves forever
httpd.serve_forever()

