// api.js will send uploaded image to FastAPI

const API_URL = "http://localhost:8000"
export async function detectGesture(blob) {
    const formData = new FormData();
    formData.append("image_file", blob, "frame.jpg");
    const response = await fetch(`${API_URL}/gesture`, {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        throw new Error("Failed to detect gesture");
    }
    return await response.json();
}