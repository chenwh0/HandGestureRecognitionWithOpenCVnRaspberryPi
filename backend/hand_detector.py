import cv2
import mediapipe

class HandDetector:
    def __init__(self):
        self.drawing_module = mediapipe.solutions.drawing_utils
        self.hands_module = mediapipe.solutions.hands

        self.model = self.hands_module.Hands()

        self.frameWidth = 640
        self.frameHeight = 480

    def detect_landmarks(self, frame):
        landmarks = []
        which_hand = None
        
        results = self.model.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for i, handLandmarks in enumerate(results.multi_hand_landmarks):
                self.drawing_module.draw_landmarks(
                    frame,
                    handLandmarks,
                    self.hands_module.HAND_CONNECTIONS
                )

                for id, pt in enumerate(handLandmarks.landmark):
                    x = int(pt.x * self.frameWidth)
                    y = int(pt.y * self.frameHeight)
                    landmarks.append([id, x, y])

                which_hand = results.multi_handedness[i].classification[0].label

        return landmarks, which_hand
