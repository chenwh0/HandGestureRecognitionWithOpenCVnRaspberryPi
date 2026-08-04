// Renders UI
import Camera from "./Camera";

function App() {
    return (
        <div class="bg-custom">
            <h1 class="text-white">Hand gesture recognition</h1>
            <small class="text-white"><em>Gesture with your fingers the numbers 1-5</em></small>
            <br></br>
            <br></br>
            <Camera />

        </div>
    );
}

export default App;