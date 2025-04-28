from common import save_image, get_file_extension_from_url
from dotenv import load_dotenv
from pathlib import Path
import os
import requests


API_IMAGES_LIMIT = 40


def fetch_nasa_images(api_key, output_directory):
    params = {
        "count": str(API_IMAGES_LIMIT),
        "api_key": api_key
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    images_links = response.json()
    photo_urls = []

    for image_info in images_links:
        file_extension = get_file_extension_from_url(image_info['url'])
        if file_extension in ('.jpeg', '.jpg'):
            photo_urls.append(image_info['url'])

    for index, photo_url in enumerate(photo_urls):
        filename = f'nasa_apod_{index}.jpg'
        save_image(photo_url, output_directory / filename)


def main():
    load_dotenv()

    nasa_token = os.environ["NASA_TOKEN"]

    images_dir = Path('images')
    images_dir.mkdir(exist_ok=True)

    fetch_nasa_images(nasa_token, images_dir)


if __name__ == '__main__':
    main()
