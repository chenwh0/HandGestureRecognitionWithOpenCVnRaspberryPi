# Know when finger is up/down based on joints

# Import needed packages
import cv2
import mediapipe

# Use MediaPipe to draw hand framework over top of hands identified in realtime
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

mod = handsModule.Hands()

frameHeight = 480
frameWidth = 640

def find_position(frame1):
    myList = [] # type: List[int]
    results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:
            drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
            list = [] # type: List[int]
            for id, pt in enumerate (handLandmarks.landmark):
                x = int(pt.x * frameWidth)
                y = int(pt.y * frameHeight)
                myList.append([id, x, y])
    return myList

def find_landmark_name(frame1):
    myList = [] # type: List[int]
    results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:
            for point in handsModule.HandLandmark:
                myList.append(str(point).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))
    return myList
