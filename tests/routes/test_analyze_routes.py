import unittest
from http import HTTPStatus
from unittest.mock import patch

from feathr_bot.app import create_app


class AnalyzeRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app(context="testing")
        self.client = app.test_client()

    @patch("feathr_bot.routes.analyze.AnalyzeService")
    def test_create_endpoint(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.analyze.return_value = "mocked result"

        response = self.client.post("/analyze/", json={"prompt": "some text"})

        self.assertEqual(response.status_code, HTTPStatus.OK)

        expected_data = {"result": "mocked result"}
        self.assertEqual(response.get_json(), expected_data)

        mock_service.assert_called_once_with(prompt="some text")
        mock_instance.analyze.assert_called_once()
