"""Chạy website Novel AI bằng Python (không cần cài thêm thư viện).

Cách dùng:
    1. Đặt file này cùng thư mục với index.html
    2. Mở terminal tại thư mục đó:  python server.py
    3. Mở trình duyệt:  http://localhost:8000
"""
import http.server
import os
import socket
import socketserver
import webbrowser

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Tắt cache để sửa index.html xong F5 là thấy ngay
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Máy tính : http://localhost:{PORT}")
    print(f"Điện thoại (cùng Wi-Fi): http://{lan_ip()}:{PORT}")
    print("Nhấn Ctrl+C để dừng.")
    webbrowser.open(f"http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng.")
