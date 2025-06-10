# Import needed packages
import cv2
from collections import Counter
from time import sleep
# Import my python files
from module import *
from ShortcutKeys import *

# Create video stream
cap = cv2.VideoCapture(0)
# Mediapipe identifies fingertips (index, middle, ring, and pinkie respectively) with the following numbers:
tipnames = [8, 12, 16, 20]

# Define 2 lists.
fingers = []  # type: List[int]
finger = []  # type: List[int]

# Infinite loop produces live feed to desktop to search for hand(s)
while True:
    ret, frame = cap.read()

    # Set frame size. 640 x 480 balances speed & accurate identification
    frame1 = cv2.resize(frame, (640, 480))

    # Get location of fingers' joints
    a = find_position(frame1)
    b = find_landmark_name(frame1)

    # Determine if finger (specifically fingertip) is up(represented by 1 in lists) or down(represented by 0 in lists)
    if len(b and a) != 0:
        finger = []
        if a[0][1:] < a[4][1:]:
            finger.append(1)
            # print to console
            print(b[4])
        else:
            finger.append(0)

        fingers = []
        for id in range(0, 4):
            if a[tipnames[id]][2:] < a[tipnames[id]-2][2:]:
                print(b[tipnames[id]])
                fingers.append(1)
            else:
                fingers.append(0)

    # Calculate fingers that are up/down
    # Concatenate 2 lists
    concatenated = fingers + finger
    # Count total number of 1s & 0s in concatenated list. Will return dictionary like {1: someNumber, 0: anotherNumber}
    totals = Counter(concatenated)
    # Get total number of 1s(fingertip ups)
    ups = totals[1]
    print("Fingers up = ", ups)

    # 1 finger up = jump to 10% of video
    if ups == 1:
        jump_10percent()
    # 2 fingers up = fullscreen
    elif ups == 2:
        fullscreen()
    # 3 fingers up = mute
    elif ups == 3:
        mute()
    # 4 fingers up = skip to next video
    elif ups == 4:
        next_video()
    # 5 fingers up = skip to next video
    elif ups == 5:
        play_pause()
    # Show current frame to desktop
    cv2.imshow("1", frame1);
    key = cv2.waitKey(1) & 0xFF
    # Press "q" to stop system
    if key == ord("q"):
        break
