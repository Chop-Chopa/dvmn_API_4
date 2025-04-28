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
    images = response.json()

    for index, image in enumerate(images):
        image_id = image["image"]
        date = image["date"].split()[0]
        year, month, day = date.split("-")

        image_url = (
            f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_id}.png"
            f"?api_key={token}"
        )

        filename = f'earth_{index}.jpg'
        save_image(image_url, directory / filename)


def main():
    load_dotenv()

    nasa_access_token = os.environ["NASA_TOKEN"]

    output_dir = Path('images')
    output_dir.mkdir(exist_ok=True)

    fetch_epic_images(nasa_access_token, output_dir)


if __name__ == '__main__':
    main()
