from collections import Counter

# Mediapipe fingertip IDs (for fingers in order: index, middle, ring, and pinkie respectively) with the following numbers:
FINGERTIPS = [8, 12, 16, 20]

def evaluate_fingers(landmark_points, which_hand):
    # Returns if each of 5 fingers (specifically fingertips) is raised (represented by 1) or down (represented by 0)
    fingers = []

    # Thumb is special bc it stretches out horizontally if "raised" 
    # thumb's joint (landmark_points[3]) is further than thumb's tip (landmark_points[4]) when thumb is raised
    if which_hand == "Right":
        if landmark_points[3][0] < landmark_points[4][0]: 
            fingers.append(1)
        else:
            fingers.append(0)
    else: # Left hand
        if landmark_points[3][0] > landmark_points[4][0]: 
            fingers.append(1)
        else:
            fingers.append(0)

    # if fingertip is vertically higher (will have lower value in OpenCV coordinates) than finger's middle joint
    for fingertip in FINGERTIPS:
        if landmark_points[fingertip][2] < landmark_points[fingertip-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

def get_raised_fingers_count(fingers):
    # Return total counts of 1s & 0s in concatenated list. Counter() returns {1: someNumber, 0: anotherNumber}
    # Get total count of 1s (finger raised)
    return Counter(fingers)[1]
