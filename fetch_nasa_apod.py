from urllib.parse import urlparse
from common import save_image
from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import os.path


API_IMAGES_LIMIT = 40


def fetch_nasa_images(token, directory):
    payload = {
        "count": str(API_IMAGES_LIMIT),
        "api_key": token
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()
    images_metadata = response.json()
    image_urls = []
    for image_metadata in images_metadata:
        path = urlparse(image_metadata['url']).path
        if os.path.splitext(path)[1] in ('.jpeg', '.jpg'):
            image_urls.append(image_metadata['url'])

    for index, img_url in enumerate(image_urls):
        filename = f'nasa_apod_{index}.jpg'
        save_image(img_url, directory / filename)


def main():
    load_dotenv()

    nasa_access_token = os.environ["NASA_TOKEN"]

    output_dir = Path('images')
    output_dir.mkdir(exist_ok=True)

    fetch_nasa_images(nasa_access_token, output_dir)


if __name__ == '__main__':
    main()
