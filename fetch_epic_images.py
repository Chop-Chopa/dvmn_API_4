from dotenv import load_dotenv
from pathlib import Path
from common import save_image
import os
import requests


def fetch_epic_images(token, directory):
    payload = {
        "api_key": token
    }
    response = requests.get("https://api.nasa.gov/EPIC/api/natural", params=payload)
    response.raise_for_status()
    images_metadata = response.json()

    for index, image_metadata in enumerate(images_metadata):
        image_id = image_metadata["image"]
        date = image_metadata["date"].split()[0]
        year, month, day = date.split("-")

        base_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_id}.png"
        params = {"api_key": token}

        response_image = requests.get(base_url, params=params)
        response_image.raise_for_status()

        filename = f'earth_{index}.jpg'
        save_image(response_image.url, directory / filename)


def main():
    load_dotenv()

    nasa_access_token = os.environ["NASA_TOKEN"]

    output_dir = Path('images')
    output_dir.mkdir(exist_ok=True)

    fetch_epic_images(nasa_access_token, output_dir)


if __name__ == '__main__':
    main()
