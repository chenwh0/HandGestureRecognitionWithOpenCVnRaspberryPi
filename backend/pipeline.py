from hand_detector import HandDetector
from gesture import evalauate_fingers, get_raised_fingers_count
class GesturePipeline:
    def __init__(self):
       self.detector = HandDetector()

    def process_frame(self, frame):
        landmarks, which_hand = self.detector.detect_landmarks(frame)
        if landmarks:
            results = {"which_hand": which_hand}
            results["finger_positions"] = evalauate_fingers(landmarks, which_hand)
            results["raised_fingers"] = get_raised_fingers_count(fingers)
            return results
        else:
            return None
