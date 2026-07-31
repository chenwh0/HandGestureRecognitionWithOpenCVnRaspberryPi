import cv2

class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture(0) # Start video stream
    def get_frame(self):
        success_status, frame = self.capture.read()
        if not success_status:
            return None
        return cv2.resize(frame, (640, 480) # 640 x 480 frame size balances speed & accurate identification
    def release(self):
        self.capture.release() # Disconnect/turn off camera
