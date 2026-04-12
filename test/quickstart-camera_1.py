import cv2
import base64
import requests

# ---- 1. Capture one frame from the MacBook camera ----
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not access the camera")

ret, frame = cap.read()
cap.release()

if not ret:
    raise RuntimeError("Failed to capture image")

image_path = "frame.jpg"
cv2.imwrite(image_path, frame)

# ---- 2. Encode image for Ollama ----
with open(image_path, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

# ---- 3. Send image to Gemma 3 Vision ----
payload = {
    "model": "gemma3:vision",
    "prompt": "Describe what you see in this image.",
    "images": [image_b64]
}

response = requests.post(
    "http://localhost:11434/api/generate",
    json=payload
)

print("\nMODEL RESPONSE:\n")
print(response.json()["response"])
