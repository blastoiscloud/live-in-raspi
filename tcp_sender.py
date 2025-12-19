import socket
import json
import base64
import cv2

GCS_IP = "10.42.0.1"
PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((GCS_IP, PORT))

def send_frame(frame, lat, lon, conf):
    _, jpg = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 60])
    payload = {
        "lat": lat,
        "lon": lon,
        "confidence": conf,
        "image": base64.b64encode(jpg).decode()
    }
    sock.sendall((json.dumps(payload) + "\n").encode())
