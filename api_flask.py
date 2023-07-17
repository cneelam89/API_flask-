from flask import Flask, request, jsonify
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

def count_black_pixels(image_url):
    try:
        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.convert("RGB")
        width, height = image.size
        pixels = image.load()
        black_pixel_count = 0

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                if r == 0 and g == 0 and b == 0:
                    black_pixel_count += 1

        return black_pixel_count

    except Exception as e:
        return str(e)

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    if not request.json or 'image_url' not in request.json:
        return jsonify({'error': 'Invalid request'}), 400

    image_url = request.json['image_url']
    black_pixel_count = count_black_pixels(image_url)

    if isinstance(black_pixel_count, str):
        return jsonify({'error': black_pixel_count}), 500

    return jsonify({'black_pixels': black_pixel_count}), 200

if __name__ == '__main__':
    app.debug = True
    app.run()
