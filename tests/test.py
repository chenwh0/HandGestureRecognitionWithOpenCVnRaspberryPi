import cv2
from pathlib import Path
from backend.pipeline import GesturePipeline

IMAGE_DIR = Path(__file__).parent / "test_images" # __file__ gets current file's path

pipeline = GesturePipeline()

def test_one_finger():
    frame = cv2.imread(f"{IMAGE_DIR}/one.jpg")
    result = pipeline.process_frame(frame)
    assert result["raised_fingers"] == 1
    assert result["action"] == "play/pause (SPACE)"

def test_fist():
    frame = cv2.imread(f"{IMAGE_DIR}/fist.jpg")
    result = pipeline.process_frame(frame)
    assert result["raised_fingers"] == 0
    assert result["action"] is None
    
def test_invalid_file():
    frame = cv2.imread(f"{IMAGE_DIR}/attributions.txt")
    result = pipeline.process_frame(frame)
    assert frame is None
    assert result["which_hand"] is None
    assert result["finger_statuses"] == []
    assert result["raised_fingers"] == 0
    assert result["action"] is None

