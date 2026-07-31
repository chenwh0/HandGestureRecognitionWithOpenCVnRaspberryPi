import math
# Mediapipe fingertip IDs (for fingers in order: index, middle, ring, and pinkie respectively) with the following numbers:
FINGERTIPS = [8, 12, 16, 20]

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def evaluate_fingers(landmark_points):
    # Returns if each of 5 fingers (specifically fingertips) is raised (represented by 1) or down (represented by 0)
    fingers = []
    raised_fingers_count = 0

    # Thumb is special bc it may also stretch out horizontally if "raised" 
    # if thumb's tip (landmark_points[4]) is further from thumb's base (landmark_points[3]) (means thumb is raised)
    if abs(landmark_points[4][0] - landmark_points[2][0]) > 10:
            fingers.append(1)
            raised_fingers_count += 1
    else:
        fingers.append(0)
    # if fingertip is vertically higher (will have lower value in OpenCV coordinates) than finger's middle joint
    for fingertip in FINGERTIPS:
        if landmark_points[fingertip][2] < landmark_points[fingertip-2][2]:
            fingers.append(1)
            raised_fingers_count += 1
        else:
            fingers.append(0)
    return fingers, raised_fingers_count
