// Display webcam, capture frames, call detectGesture(frameBlob), show returned results
import { useEffect, useRef, useState } from "react";
import { detectGesture } from "./api";
import './Camera.css'

function Camera() {
    const videoRef = useRef(null); // Create reference to <video> element
    const canvasRef = useRef(null);
    const intervalRef = useRef(null);

    const [detecting, setDetecting] = useState(false);
    const [result, setResult] = useState(null);

    useEffect(() => {
        async function startCamera() {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true }); // Ask for webcam access
            videoRef.current.srcObject = stream;
        }
        startCamera();
        return () => {
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
        };
    }, []);

    // Function to capture current video frame 
    async function captureFrame() {
        const canvas = canvasRef.current;
        const video = videoRef.current;
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        
        const context = canvas.getContext("2d");
        context.drawImage(video, 0, 0, canvas.width, canvas.height); // Copy current frame onto canvas
        
        const blob = await new Promise((resolve) => {
            canvas.toBlob(resolve, "image/jpeg");
        }); // convert canvas with frame into image blob

        const response = await detectGesture(blob);
        console.log("API response:", response);
        console.log(video.videoWidth, video.videoHeight);
        setResult(response);
    }

    function toggleDetection() {
        if (detecting) {
            clearInterval(intervalRef.current);
            intervalRef.current = null;
            setDetecting(false);
        }
        else {
            intervalRef.current = setInterval(() => {
                captureFrame();
            }, 500); // send every 500ms (2 frames per sec)
            setDetecting(true);
        }
    }
    return (
        <>
        <div className="content-container">
            <div className="recording-container">
                <video className="video-custom" ref={videoRef} autoPlay playsInline muted/>
                <canvas ref={canvasRef} style={{ display: "none" }}/>
                <button className="btn btn-custom px-3 my-2" onClick={toggleDetection}>{detecting ? "Stop ⏺️" : "Detect ▶️"}</button>
            </div>
            <div className="result-container">
                {result && (<div className="result">
                    <h3>Last gesture & Shortcut action sent</h3>
                    <p>Hand: {result.which_hand}</p>
                    <p>Fingers raised: {result.finger_statuses}</p>
                    <p>Total raised: {result.raised_fingers}</p>
                    <p>Action: {result.action}</p>
                </div>)}
            </div>
        </div>
        </>
    );
}

// Display webcam in <video>. Draw current video frame onto canvas, convert canvas to image (blob), send blob to FastAPI


export default Camera;