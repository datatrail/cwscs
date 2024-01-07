import logging
import os
from unittest.mock import patch

import pytest

from cwscs.storage import Storage


class TestStorage:
    @pytest.fixture
    def storage(self, tmpdir):
        return Storage(str(tmpdir))

    def test_storage_init(self, storage):
        assert os.path.exists(storage.path)
        assert os.path.exists(storage.search_path)
        assert os.path.exists(storage.lots_path)
        assert os.path.exists(storage.auctions_path)
        assert os.path.exists(storage.bids_path)

    @patch("os.makedirs")
    @patch("os.path.exists")
    def test_setup_path_existing_path(self, mock_path_exists, mock_os_makedirs, caplog, storage):
        mock_path_exists.return_value = True
        mock_os_makedirs.return_value = None
        caplog.set_level(logging.INFO)
        Storage._setup_path(storage.path)
        assert mock_os_makedirs.call_count == 0
        for record in caplog.records:
            assert record.levelname == "INFO"

        # assert "already exists" in caplog.text
        # with patch("os.makedirs") as mock_makedirs:
        #     mock_makedirs.return_value = None
        #     Storage._setup_path(storage.path)
        #     assert mock_makedirs.call_count == 0
        #     assert "already exists" in caplog.text

    # def test_setup_path_nonexistent_path(self, caplog, storage):
    #     with patch('storage_module.os.makedirs') as mock_makedirs:
    #         Storage._setup_path(storage.path)
    #         assert mock_makedirs.call_count == 1
    #         assert "Successfully created directory" in caplog.text

    # def test_get_lots(self, storage):
    #     with patch('storage_module.Lot') as mock_lot:
    #         mock_lot_instance = mock_lot.return_value
    #         mock_lot_instance.bidding_end_time = '2022-01-01T00:00:00'

    #         for lot_id in range(1, 4):
    #             lot_file_name = f"lot-{lot_id}.html"
    #             lot_file_path = os.path.join(storage.lots_path, lot_file_name)
    #             with open(lot_file_path, 'w') as f:
    #                 f.write(f"Dummy content for lot {lot_id}")

    #         lots = storage.get_lots()

    #         assert len(lots) == 3
    #         assert all(isinstance(lot, mock_lot) for lot in lots)

    # def test_update_lots(self, storage):
    #     with patch('storage_module.Lot') as mock_lot:
    #         mock_lot_instance = mock_lot.return_value
    #         mock_lot_instance.bidding_end_time = '2022-01-01T00:00:00'

    #         for lot_id in range(1, 4):
    #             lot_file_name = f"lot-{lot_id}.html"
    #             lot_file_path = os.path.join(storage.lots_path, lot_file_name)
    #             with open(lot_file_path, 'w') as f:
    #                 f.write(f"Dummy content for lot {lot_id}")

    #         storage.update_lots()

    #         assert mock_lot_instance.update.call_count == 3

    # def test_info(self, capfd, storage):
    #     storage.info()
    #     out, _ = capfd.readouterr()
    #     assert f"Properties of {storage.__class__.__name__}:" in out
    #     assert f"- path: {storage.path}" in out
    #     assert f"- search_path: {storage.search_path}" in out
    #     assert f"- lots_path: {storage.lots_path}" in out
    #     assert f"- auctions_path: {storage.auctions_path}" in out
    #     assert f"- bids_path: {storage.bids_path}" in out
