from flask import Flask, jsonify
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

IMAGE_URL = "PUT_YOUR_IMAGE_URL_HERE"

@app.route("/")
def home():
    return "Pixel API running"

@app.route("/pixels")
def pixels():
    try:
        r = requests.get(IMAGE_URL, timeout=10)
        r.raise_for_status()

        img = Image.open(BytesIO(r.content)).convert("RGB")

        width, height = img.size
        pixels = img.load()

        data = {}
        index = 1

        for y in range(height):
            for x in range(width):
                data[f"Pixel_{index}"] = list(pixels[x, y])
                index += 1

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
