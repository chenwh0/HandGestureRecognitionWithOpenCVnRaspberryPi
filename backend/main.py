from fastapi import FastAPI
from pipeline import GesturePipeline

app = FastAPI()
pipeline = GesturePipeline()

@app.post("/gesture")
def detect_gesture(frame):
    result = pipeline.process_frame(frame)
    return result

@app.get("/health")
def health():
    return {"status": "running"}

