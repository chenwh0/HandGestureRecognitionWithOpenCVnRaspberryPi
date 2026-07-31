from .hand_detector import HandDetector
from .gesture import evaluate_fingers
from .shortcut_keys import run_shortcut

class GesturePipeline:
    def __init__(self):
       self.detector = HandDetector()

    def process_frame(self, frame):
        results = {
            "which_hand": None,
            "finger_statuses": [],
            "raised_fingers": 0,
            "action": None
        }
        if frame is None:
            return results
        
        landmarks, which_hand = self.detector.detect_landmarks(frame)
        if landmarks:
            results["which_hand"] = which_hand
            results["finger_statuses"], results["raised_fingers"] = evaluate_fingers(landmarks)
            results["action"] = run_shortcut(results["raised_fingers"])
        return results
