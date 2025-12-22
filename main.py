from flask import Flask, jsonify
from PIL import Image
import requests
from io import BytesIO
import os

app = Flask(__name__)

# Put your GitHub raw image URL here
IMAGE_URL = "https://github.com/Kilua399/Game/raw/main/image.jpeg"

@app.route("/")
def home():
    return "Server is running"

@app.route("/pixels")
def pixels():
    # Download the image
    response = requests.get(IMAGE_URL)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    # Optional: resize to reduce JSON size
    img = img.resize((64, 64))

    width, height = img.size
    pixels = img.load()

    pixel_table = {}
    index = 1

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixel_table[f"Pixel_{index}"] = [r, g, b]
            index += 1

    return jsonify({
        "width": width,
        "height": height,
        "pixels": pixel_table
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
