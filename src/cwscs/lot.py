import json

from cwscs.webpage import Webpage


class Lot(Webpage):
    def __init__(self, id: int):
        self.id = id
        self._html = ""
        self._json_v1 = ""
        self._json_v3 = ""

    @property
    def url(self):
        return f"{self.BASE_URL}/l/{self.id}"

    @property
    def url_api_v1(self):
        return f"{self.API_URL}/v1/lots?ids={self.id}&locale=nl"

    @property
    def url_api_v3(self):
        return f"{self.API_URL}/v3/bidding/lots?ids={self.id}&locale=nl"

    def update(self, file_path: str, replace: bool = True):
        self._update_html(file_path, replace)
        self._update_json_v1(file_path, replace)
        self._update_json_v3(file_path, replace)

    def _update_html(self, file_path: str, replace: bool = True):
        file_path = f"{file_path}/lot-{self.id}.html"
        self.update_content(self.url, file_path, replace)
        self._html = self._read_text(file_path)

    def _update_json_v1(self, file_path: str, replace: bool = True):
        file_path = f"{file_path}/lot-v1-{self.id}.json"
        self.update_content(self.url_api_v1, file_path, replace)
        self._json_v1 = self._read_text(file_path)
        self._extract_properties_json_v1()

    def _update_json_v3(self, file_path: str, replace: bool = True):
        file_path = f"{file_path}/lot-v3-{self.id}.json"
        self.update_content(self.url_api_v3, file_path, replace)
        self._json_v3 = self._read_text(file_path)
        self._extract_properties_json_v3()

    def _extract_properties_json_v1(self):
        data_v1 = json.loads(self._json_v1)
        if len(data_v1["lots"]) > 0:
            self.title = data_v1["lots"][0]["title"]
            self.thumbnail2_url = data_v1["lots"][0]["thumbnail2_url"]
            self.pubnub_channel = data_v1["lots"][0]["pubnub_channel"]
            self.auction_id = data_v1["lots"][0]["auction_id"]
            self.explicit_content = data_v1["lots"][0]["explicit_content"]
            self.is_content_explicit = data_v1["lots"][0]["is_content_explicit"]
            self.original_image_url = data_v1["lots"][0]["original_image_url"]
        else:
            self.title = None
            self.thumbnail2_url = None
            self.pubnub_channel = None
            self.auction_id = None
            self.explicit_content = None
            self.is_content_explicit = None
            self.original_image_url = None

    def _extract_properties_json_v3(self):
        data_v3 = json.loads(self._json_v3)
        if len(data_v3["lots"]) > 0:
            self.highest_bidder_token = data_v3["lots"][0]["highest_bidder_token"]
            self.winner_token = data_v3["lots"][0]["winner_token"]
            self.current_bid_amount = data_v3["lots"][0]["current_bid_amount"]["EUR"]
            self.bidding_start_time = data_v3["lots"][0]["bidding_start_time"]
            self.bidding_end_time = data_v3["lots"][0]["bidding_end_time"]
            self.reserve_price_met = data_v3["lots"][0]["reserve_price_met"]
            self.favorite_count = data_v3["lots"][0]["favorite_count"]
            self.closed = data_v3["lots"][0]["closed"]
            self.realtime_channel = data_v3["lots"][0]["realtime_channel"]
            self.meta_time = data_v3["meta"]["time"]
        else:
            self.highest_bidder_token = None
            self.winner_token = None
            self.current_bid_amount = None
            self.bidding_start_time = None
            self.bidding_end_time = None
            self.reserve_price_met = None
            self.favorite_count = None
            self.closed = None
            self.realtime_channel = None
            self.meta_time = None
