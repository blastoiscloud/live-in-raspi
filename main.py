import asyncio
import cv2
from gps_reader import GPSReader
from camera import open_gopro
from ai_detector import detect_stress
from tcp_sender import send_frame

async def main():
    gps = GPSReader()
    await gps.connect()

    cap = open_gopro()

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        stress, conf = detect_stress(frame)

        if stress and gps.lat:
            print(f"🌱 Stress detected @ {gps.lat}, {gps.lon}")
            send_frame(frame, gps.lat, gps.lon, conf)

        cv2.waitKey(1)

asyncio.run(main())
