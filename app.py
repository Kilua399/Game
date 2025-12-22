from flask import Flask, jsonify
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

# 🔗 IMAGE URL (PUT YOUR IMAGE LINK HERE)
IMAGE_URL = "https://github.com/Kilua399/Game/blob/main/UsingNow.jpeg?raw=true"

def get_pixels():
    response = requests.get(IMAGE_URL)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    width, height = img.size
    pixels = img.load()

    pixel_table = {}
    index = 1

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixel_table[f"Pixel_{index}"] = [r, g, b]
            index += 1

    return pixel_table

@app.route("/")
def home():
    return "Pixel API running"

@app.route("/pixels")
def pixels():
    return jsonify(get_pixels())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
