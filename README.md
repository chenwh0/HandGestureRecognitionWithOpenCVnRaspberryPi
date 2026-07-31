# Use Hand Gestures to run commands on your computer

# Demo video (click to play)
[![image](https://github.com/user-attachments/assets/b44d4aad-9da5-4fe6-b881-7771b8abab48)](https://www.youtube.com/watch?v=UbaJz3TvRb4)

## Description
This project can detect various hand gestures from a pi camera and run specific command(s) on the computer based on the correct hand gesture recognized! The recognition of various hand gestures is implemented using MediaPipe and OpenCV. Specifically, this was applied to toggle YouTube media controll buttons using hand gestures instead of keyboard shortcuts.
This project is beneficial to those with disabilities, those who aren’t close to their computers, or those who just want a simple hand gesture to quickly run a certain a set of mundane tasks on the computer.

## Features

✌️ Finger gesture recognition

🕦 Real-time hand tracking using MediaPipe

⌨️ Keyboard automation using pynput

🖥️ FastAPI REST API

## API

### POST /gesture

Input:

[.png or .jpg file]

Output:

```
{
    "which_hand": "Left",
    "finger_statuses": [0, 1, 1, 1, 0],
    "raised_fingers": 3,
    "action": "mute (m)"
}
```
## Testing
Tests in `tests/` directory and use sample hand gesture images and files to validate the gesture recognition pipeline.

✅ Test with 1-finger up image

✅ Test with fist up image

✅ Test with invalid file
