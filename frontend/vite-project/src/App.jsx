// Renders UI
import Camera from "./Camera";
import "./App.css";

function App() {
    return (
        <div class="bg-custom">
            <h1 class="text-white">Hand gesture recognition</h1>
            <small className="text-white custom-subtitle"><em>Gesture 1–5 fingers to test detection here.</em> Then open to any <a href="https://www.youtube.com/">YouTube</a> video to control it with same gestures.</small>
            <br></br>
            <br></br>
            <Camera />

        </div>
    );
}

export default App;