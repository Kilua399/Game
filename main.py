from flask import Flask, jsonify
from PIL import Image
import os

app = Flask(__name__)

IMAGE_PATH = "https://github.com/Kilua399/Game/blob/main/image.jpeg?raw=true"

@app.route("/")
def home():
    return "Server is running"

@app.route("/pixels")
def pixels():
    img = Image.open(IMAGE_PATH).convert("RGB")

    # OPTIONAL: Resize to avoid Roblox limits
    img = img.resize((64, 64))

    width, height = img.size
    px = img.load()

    data = {}
    i = 1

    for y in range(height):
        for x in range(width):
            r, g, b = px[x, y]
            data[f"Pixel_{i}"] = [r, g, b]
            i += 1

    return jsonify({
        "width": width,
        "height": height,
        "pixels": data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

