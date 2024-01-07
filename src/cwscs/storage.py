import logging
import os

from cwscs.lot import Lot


class Storage(object):
    def __init__(self, path: str) -> None:
        self.path = self._setup_path(path)
        self.search_path = self._setup_path(os.path.join(path, "search"))
        self.lots_path = self._setup_path(os.path.join(path, "lots"))
        self.auctions_path = self._setup_path(os.path.join(path, "auctions"))
        self.bids_path = self._setup_path(os.path.join(path, "bids"))

    @staticmethod
    def _setup_path(path):
        if os.path.exists(path):
            logging.info(f"{path} already exists")
        else:
            os.makedirs(path)
            logging.info(f"Successfully created directory {path}")
        return os.path.abspath(path)

    def get_lots(self):
        lots = []
        for file_name in os.listdir(self.lots_path):
            if file_name.startswith("lot-") and file_name.endswith(".html"):
                lot_id = file_name.split("-")[1].split(".")[0]
                lot = Lot(lot_id)
                lot.update(self.lots_path, replace=False)
                if lot.bidding_end_time is not None:
                    lots.append(lot)
        lots.sort(key=lambda x: x.bidding_end_time)
        return lots

    def update_lots(self, replace: bool = True):
        for lot in self.get_lots():
            if not lot.closed:
                lot.update(self.lots_path, replace=replace)



    def info(self) -> None:
        print(f"Properties of {self.__class__.__name__}:")
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                print(f"- {key}: {value}")
