from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).parent


class StoreHandler(SimpleHTTPRequestHandler):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, directory=ROOT, **kwargs)


if __name__ == "__main__":
	server = ThreadingHTTPServer(("127.0.0.1", 8000), StoreHandler)
	print("iPhone store running at http://127.0.0.1:8000")
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("\nServer stopped")
		server.server_close()
