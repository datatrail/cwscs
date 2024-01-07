import json
from typing import List

from bs4 import BeautifulSoup
from webpage import Webpage


class Auction(Webpage):
    def __init__(self, id: int):
        self.id = id
        self._html = ""
        self._json_v1 = ""
        self.lot_ids: List[int] = []

    @property
    def url(self):
        return f"{self.BASE_URL}/a/{self.id}"

    @property
    def url_api_v1(self):
        return f"{self.API_URL}/v1/auctions?ids={self.id}&locale=nl"

    def update(self, file_path: str, replace: bool = True):
        self._update_html(file_path, replace)
        self._update_json_v1(file_path, replace)

    def _update_html(self, file_path: str, replace: bool = True):
        file_path = f"{file_path}/auction-{self.id}.html"
        self.update_content(self.url, file_path, replace)
        self._html = self._read_text(file_path)
        self._extract_lot_ids()

    def _extract_lot_ids(self):
        soup = BeautifulSoup(self._html, "lxml")
        slugs = [a["href"] for a in soup.find_all("a", class_="c-lot-card")]
        ids = [slug.split("/l/")[1].split("-")[0] for slug in slugs]
        self.lot_ids = ids

    def _update_json_v1(self, file_path: str, replace: bool = True):
        file_path = f"{file_path}/auction-v1-{self.id}.json"
        self.update_content(self.url_api_v1, file_path, replace)
        self._json_v1 = self._read_text(file_path)
        self._extract_properties_json_v1()

    def _extract_properties_json_v1(self):
        json_data = json.loads(self._json_v1)
        if len(json_data["auctions"]) > 0:
            props = json_data["auctions"][0]
            self.close_at = props["close_at"]
            self.closed_at = props["closed_at"]
            self.start_at = props["start_at"]
            self.lot_count = props["lot_count"]
            self.number_of_lots = props["number_of_lots"]
            self.title = props["title"]
            self.type_id = props["type_id"]
            self.theme_id = props["theme_id"]
            self.themed = props["themed"]
            self.explicit_content = props["explicit_content"]
            self.status = props["status"]
            self.has_context = props["has_context"]
        else:
            self.close_at = None
            self.closed_at = None
            self.start_at = None
            self.lot_count = None
            self.number_of_lots = None
            self.title = None
            self.type_id = None
            self.theme_id = None
            self.themed = None
            self.explicit_content = None
            self.status = None
            self.has_context = None
