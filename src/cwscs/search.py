from typing import List

from bs4 import BeautifulSoup
from webpage import Webpage


class Search(Webpage):
    def __init__(self, keyword: str):
        self.keyword = keyword
        self._html = ""
        self.lot_ids: List[int] = []

    @property
    def url(self):
        return f"{self.BASE_URL}/se?q={self.keyword}"

    def update(self, file_path: str, replace: bool = True):
        self._update_html(file_path, replace)

    def _update_html(self, file_path: str, replace: bool = True):
        file_path = f"{file_path}/search-{self.keyword}.html"
        self.update_content(self.url, file_path, replace)
        self._html = self._read_text(file_path)
        self._extract_lot_ids()

    def _extract_lot_ids(self):
        soup = BeautifulSoup(self._html, "lxml")
        slugs = [a["href"] for a in soup.find_all("a", class_="c-lot-card")]
        ids = [slug.split("/l/")[1].split("-")[0] for slug in slugs]
        self.lot_ids = ids

    def __str__(self):
        return self.keyword
