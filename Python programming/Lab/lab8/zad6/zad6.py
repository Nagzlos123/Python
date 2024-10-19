#!/usr/bin/env python3
# Przyklad tworzy prosty serwer www wykorzystujac klase simpleHTTPRequestHandler
import http.server, socketserver
PORT = 11022
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serwer wystartowal na porcie ", PORT)
    httpd.serve_forever()

