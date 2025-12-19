import cv2

def open_gopro():
    # USB webcam mode OR RTSP
    cap = cv2.VideoCapture(0)  # USB
    # OR RTSP:
    # cap = cv2.VideoCapture("udp://0.0.0.0:8554")

    if not cap.isOpened():
        raise RuntimeError("GoPro not detected")

    return cap
