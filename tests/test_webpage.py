import os
from unittest.mock import patch

from cwscs.webpage import Webpage


class TestWebpage:
    @patch("cwscs.webpage.Webpage.download_webpage")
    @patch("os.path.exists")
    def test_update_content_replace_true(self, mock_path_exists, mock_download_webpage):
        # arrange
        webpage = Webpage()
        url = "https://www.catawiki.com/nl/se?q=buth"
        file_path = "tests/testdata/search-buth/search-buth.html"
        replace = True

        mock_path_exists.return_value = True
        mock_download_webpage.return_value = True

        # act
        webpage.update_content(url, file_path, replace)

        # assert
        mock_download_webpage.assert_called_once_with(url, file_path)

    @patch("cwscs.webpage.Webpage.download_webpage")
    @patch("os.path.exists")
    def test_update_content_replace_false(self, mock_path_exists, mock_download_webpage):
        # arrange
        webpage = Webpage()
        url = "https://www.catawiki.com/nl"
        file_path = "tests/testdata/test.html"
        replace = False

        mock_path_exists.return_value = True
        mock_download_webpage.return_value = True

        # act
        webpage.update_content(url, file_path, replace)

        # assert
        mock_download_webpage.assert_not_called()

    @patch("requests.get")
    def test_download_webpage_status_200(self, mock_requests_get, tmp_path):
        # arrange
        webpage = Webpage()
        url = "https://www.catawiki.com/nl"
        file_path = tmp_path / "file_status_200.txt"
        time_out = 0

        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.text = "webpage content"

        # act
        webpage.download_webpage(url, file_path, time_out)

        # assert
        fread = file_path
        mock_requests_get.assert_called_once_with(url)
        assert fread.read_text() == "webpage content"

    @patch("requests.get")
    def test_download_webpage_status_404(self, mock_requests_get, tmp_path):
        # arrange
        webpage = Webpage()
        url = "https://www.catawiki.com/nl"
        file_path = tmp_path / "file_status_404.txt"
        time_out = 0

        mock_requests_get.return_value.status_code = 404

        # act
        webpage.download_webpage(url, file_path, time_out)

        # assert
        mock_requests_get.assert_called_once_with(url)
        assert os.path.exists(file_path) is False

    def test_download_webpage_exception(self, tmp_path, caplog):
        # arrange
        webpage = Webpage()
        url = None
        file_path = tmp_path / "file_exception.txt"
        time_out = 0

        # act
        webpage.download_webpage(url, file_path, time_out)

        # assert
        for record in caplog.records:
            assert record.levelname == "ERROR"
        assert "Invalid URL 'None'" in caplog.text
