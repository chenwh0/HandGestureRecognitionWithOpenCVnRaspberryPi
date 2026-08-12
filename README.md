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

📸 FastAPI REST API (send images instead of live detection)

🖥️ Responsive React UI for webcam access, gesture detection, and action execution

📋 Automated backend tests using pytest


# Setup

## Backend

1. Download repo then open Terminal from inside root folder. 

2. Install dependencies - `pip install -r requirements.txt`

3. Start FastAPI server at root folder by entering into the Terminal - `python -m uvicorn backend.main:app --reload`

4. Interactive API at http://localhost:8000/docs

## Frontend

1. Open new Terminal window and go to frontend folder - `cd frontend`

2. Install Node Package Manager - `npm install`

3. Run Node Package Manager - `npm run dev`

4. Click on http://localhost:5173 URL in Terminal window to open the UI.

5. Accept turning on of webcam.

6. Click "Detect ▶️" button.

7. Open to any [YouTube](https://www.youtube.com/) video in your browser and start gesturing! 

8. Click "Stop ⏺️" button to end. 


# API

## ```POST /gesture```
Accepts image and returns action associated with detected gesture.

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

## ```GET /health```

Check if backend is running.

Output:

```
{
    "status": "running"
}
```

# Testing

1. Travel to root folder

2. Run ```pip install -r requirements.txt```

3. Run ```pytest test_pipeline.py```

Tests:

✅ Test with 1-finger up image

✅ Test with fist up image

✅ Test with invalid file