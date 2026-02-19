from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import subprocess
import os

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running 🥀")

def run_server():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

def run_bot():
    subprocess.run(["python3", "main.py"])

threading.Thread(target=run_bot).start()
run_server()