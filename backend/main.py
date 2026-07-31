from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
from .pipeline import GesturePipeline
from .schemas import GestureResponse  

app = FastAPI()

# Let React frontend communicate with FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
pipeline = GesturePipeline()


# Routes
@app.post("/gesture", response_model=GestureResponse) # send image to this URL
# Define asynchronous function so that program's other functions can still run if this function is paused.
# File(...) means file input required.
async def detect_gesture(image_file: UploadFile=File(...)):
    contents = await image_file.read()
    image_array = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    if frame is None:
        raise HTTPException(status_code=400, detail="Invalid image file")
    return pipeline.process_frame(frame)

@app.get("/health")
def health():
    return {"status": "running"}

