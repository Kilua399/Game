from flask import Flask, jsonify
from PIL import Image
import requests
from io import BytesIO
import os

app = Flask(__name__)

Image.MAX_IMAGE_PIXELS = None  # disable safety limit
IMAGE_URL = "https://www.dropbox.com/scl/fi/gwqy41r0f2n1s1m07voqf/Best-One-Wael-New.jpg?rlkey=z0i7pjjv3zadd3p9r2y48rqok&st=9wd8zwts&dl=1"

@app.route("/")
def home():
    return "Server is running"

@app.route("/pixels")
def pixels():
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

    return jsonify({
        "width": width,
        "height": height,
        "pixels": pixel_table
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



