import cv2
from camera import Camera
from pipeline import GesturePipeline

camera = Camera()
pipeline = GesturePipeline()

while True:
    frame = camera.get_frame()
    result = pipeline.process_frame(frame)
    if result:
        print(result)
        
    cv2.imshow("Hand Gesture", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()
