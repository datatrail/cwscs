import logging
import os
import time

import requests


class Webpage(object):
    BASE_URL = "https://www.catawiki.com/nl"
    API_URL = "https://www.catawiki.com/buyer/api"

    @staticmethod
    def update_content(url: str, file_path: str, replace: bool = True) -> None:
        if os.path.exists(file_path) and not replace:
            logging.info(f"{url} already saved to ({file_path})")
        else:
            Webpage.download_webpage(url, file_path)

    @staticmethod
    def download_webpage(url: str, file_path: str, time_out: int = 5) -> None:
        time.sleep(time_out)
        try:
            response = requests.get(url)

            if response.status_code == 200:
                with open(file_path, "w", encoding="utf-8") as output_file:
                    output_file.write(response.text)
                logging.info(f"Successfully downloaded {url} and saved to {file_path}")
            else:
                logging.error(f"Failed tooo download {url}. Status code: {response.status_code}")

        except Exception as e:
            logging.error(f"An error occurred: {e}")

    @staticmethod
    def _read_text(file_path: str):
        with open(file_path, "r", encoding="utf8") as file:
            return file.read()

    def info(self) -> None:
        print(f"Properties of {self.__class__.__name__}:")
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                print(f"- {key}: {value}")
