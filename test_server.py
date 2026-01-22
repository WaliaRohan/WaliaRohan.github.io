import http.server
import socketserver
import os

PORT = 8000
# Change to a specific directory if needed, otherwise it serves the script's directory
# os.chdir('/path/to/your/files') 

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}. Join at http://localhost:{PORT}")
    httpd.serve_forever()