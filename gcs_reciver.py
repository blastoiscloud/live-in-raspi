import socket
import json
import base64

PORT = 6000
points = []

sock = socket.socket()
sock.bind(("", PORT))
sock.listen(1)
conn, _ = sock.accept()

print("🛰 GCS Connected")

while True:
    data = conn.recv(10_000)
    if not data:
        break

    for line in data.splitlines():
        pkt = json.loads(line)
        points.append((pkt["lat"], pkt["lon"], pkt["confidence"]))
