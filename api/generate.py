from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs


def simple_ascii(text):
    """ASCII generator sederhana tanpa library eksternal."""
    border = "*" * (len(text) + 4)
    return f"{border}\n* {text} *\n{border}"


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Ambil query parameter
        query = parse_qs(urlparse(self.path).query)
        text = query.get("text", [""])[0]

        # ASCII processing
        ascii_art = simple_ascii(text)

        # Response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps({"ascii": ascii_art}).encode())
