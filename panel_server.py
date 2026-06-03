from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parent
PANEL = ROOT / "SESION_GUIADA.html"
PORT = 8765


class PanelHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path == "/events":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.end_headers()

            last_mtime = PANEL.stat().st_mtime if PANEL.exists() else 0

            while True:
                try:
                    current_mtime = PANEL.stat().st_mtime if PANEL.exists() else 0
                    if current_mtime != last_mtime:
                        last_mtime = current_mtime
                        self.wfile.write(b"event: reload\n")
                        self.wfile.write(b"data: updated\n\n")
                        self.wfile.flush()
                    else:
                        self.wfile.write(b"event: ping\n")
                        self.wfile.write(b"data: alive\n\n")
                        self.wfile.flush()

                    time.sleep(0.5)
                except (BrokenPipeError, ConnectionResetError):
                    break
            return

        return super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), PanelHandler)
    print(f"Panel activo: http://127.0.0.1:{PORT}/SESION_GUIADA.html")
    server.serve_forever()
