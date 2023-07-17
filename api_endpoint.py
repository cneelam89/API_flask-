import requests
import json

url = 'http://localhost:5000/analyze_image'
# image_url = 'F:/html/images/1.jpg'
image_url = 'https://www.seiu1000.org/sites/main/files/main-images/camera_lense_0.jpeg'

payload = {
    'image_url': image_url
}

response = requests.post(url, json=payload)
data = response.json()

if response.status_code == 200:
    black_pixels = data['black_pixels']
    print(f"Number of black pixels: {black_pixels}")
else:
    error_message = data['error']
    print(f"Error: {error_message}")