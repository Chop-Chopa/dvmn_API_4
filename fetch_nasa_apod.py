from urllib.parse import urlparse
from common import save_image
from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import os.path


def fetch_nasa_image(token, directory):
    payload = {
        "count": "40",
        "api_key": token
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()
    image_response = response.json()
    images_link = []
    for image in range(len(image_response)):
        path = urlparse(image_response[image]['url']).path
        if os.path.splitext(path)[1] == '.jpeg' or os.path.splitext(path)[1] == '.jpg':
            images_link.append(image_response[image]['url'])

    for index, img_url in enumerate(images_link):
        filename = f'nasa_apod_{index}.jpg'
        save_image(img_url, directory / filename)


def main():
    load_dotenv()

    nasa_acess_token = os.environ["NASA_TOKEN"]

    output_dir = Path('images')
    output_dir.mkdir(exist_ok=True)

    fetch_nasa_image(nasa_acess_token, output_dir)


if __name__ == '__main__':
    main()
