from flask import Blueprint, Response
import cv2
from app.models.realtime import apply_filter

video = Blueprint("video", __name__)

def gen_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = apply_filter(frame)

        # ✅ ADD THIS
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        _, buffer = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


@video.route("/video")
def video_stream():
    return Response(gen_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame')