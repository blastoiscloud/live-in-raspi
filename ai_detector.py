import random

def detect_stress(frame):
    """
    Replace this with:
    - YOLOv8
    - NDVI model
    - CNN
    """
    detected = random.random() > 0.97  # simulate stress
    confidence = round(random.uniform(0.7, 0.95), 2)

    return detected, confidence
