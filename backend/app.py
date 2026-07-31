import cv2
from camera import Camera
from pipeline import GesturePipeline
from shortcut_keys import run_shortcut

camera = Camera()
pipeline = GesturePipeline()

while True:
    frame = camera.get_frame()
    result = pipeline.process_frame(frame)
    if result:
        print("Raised fingers:", result["raised_fingers"])
        run_shortcut(result["raised_fingers"])
    
    cv2.imshow("Hand Gesture", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()
