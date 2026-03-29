import cv2

def apply_filter(frame):
    # Simple safe filter (no mediapipe for now)
    return cv2.stylization(frame, sigma_s=60, sigma_r=0.5)