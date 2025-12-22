from flask import Flask, jsonify
from PIL import Image
import requests
from io import BytesIO
import os

app = Flask(__name__)

# Put your GitHub raw image URL here
IMAGE_URL = "https://previews.dropbox.com/p/thumb/AC0Hv9yN2XzOV8i_EYZqWfyXVNkKupk2wLX1Qhg7vfgnt6eLSsQeOT1fzC9wxGEMqpsBd1LDVGVAecLtkv9Wf3B2o_MgcQLY6EXNzHggTxM8HmwJpCPhLJOAmLexZrk7cQw240uiyCZP2tHXY5wqEpe3A_UO7PSRYx0jj9K_8Xsen6Z1S9V14rqEc1uQeMdp8rFyXyJz8A_0tNN5ShUHLa-HyRQRoQgJ2lNrTIqtAaCcU0yws6_rdYc3fKG-cDVTzPHUMeFeF7THD3PEFnAU2GN5-STdNYXU8WvSY1o5ayrkr6QBfu4-jF-rGIsNRQbf96_eVVLjKdqURsm0AZLegIAA5oLuYNfzKcccDV8z3MkoqftORanU6WtX10KjZodD5HIsXriKOIgNhGfUO__Gcp1ZsJLswcibhEdHxNeXTw7sBYtYglqW0vYSpBj-RPLKGDt-w_GUfebRqzF8tSkRqfB1Pb-lQotTFt2OGB_jqQ6jWFFcsrFZIivfgDHIeID9jQr4vONc5aNZOA3c4NvQwazs3QiPy_V2X4tYaonN2PQk1jm_pzG-TcvStNEfsrXpCd52tYuPjogw_JDnIXiqWS3FllDzgIeGQ-25EYC2fEpAE4LazSOqvtUpskCJFUnRCcLLFDW3D0Xi1bkuIcL9Bat-gery7JlUi4V2rOy6dzUZBwGfeoZf7UNlKvfO5FtEYfxbXQH5uwfwT2j91yk0RRwO8ua13zmSsj7zX4OuIKEcZX3s0MnOF00fm29HhpGwOEVhTyLD2K5iPj74WClUya6KUWm9aLGnVy4A3BU6BXkKyYVM95zs0bCinrMBarC_RFk6_mha8z0tPrVWg7faUFmPJNfOZVtW27exkAHYl60fVvXG829GK2IFwUry5h_RVRLcY1ZNlH24wB5IQ6hUvClNunOLrzNGKqKLDlcelwXMf_vdBbyQoYTZP6oaYG00I2dHYFujMZCK15USaU71iHW_XNsTmt3jGwkScnibW_DyBfiCEBuvvsMT66xzo77hKxb_Gm6MprYqJ-vR6ZC5qJ12zCYJBGPAxpB2ZC014bAlg9-22jtUx4VDF1gWeudRtUdbKK7hfkRdADQ7Nz5vzV99OqROXlBBpsDCdpUOyW4BxDjmMt0dXgKNE4PN0BZqxunBpC7PV-xOQy9ZJ_6pm1VpU9btLgUZb2-EooteACSB_X25Zt7kbOoymE-64UauRPHlzlR-nUYg2GxXd4RYJ0DdM-fo49sYXDlral-u9F_vObohHIAUvkShtM847eOopxMG4Wsk9raJ1YoMdmy9Uh9iusOWLqYk-nhLKvyHGQWQvspgdgBPMTkZQbIcNNQnTWzgEp3z5ewqIp7KvJ3tlbqQZ_v46afS457mpawbqnWGmPraScm9E7yK7njbXz6XwGdABdkbxswEndDpTRv4dRr9rF92KK_sTFB8k-9Ek4nJE6yWbUBIuwJgWKKRrOX7wuiHV5zAeFiYXWJky-F9pY89HaKzf5ZmpCMj2kp3viGHaJuVAiinQotWOvmuFaUB-MoOl_lpeXxR0p6j1X1-Bgi5/p.jpeg?is_prewarmed=true"

@app.route("/")
def home():
    return "Server is running"

@app.route("/pixels")
def pixels():
    # Download the image
    response = requests.get(IMAGE_URL)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    # Optional: resize to reduce JSON size
    #img = img.resize((64, 64))

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


