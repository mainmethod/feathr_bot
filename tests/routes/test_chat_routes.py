import unittest
from http import HTTPStatus
from unittest.mock import patch
from feathr_bot.app import create_app
from feathr_bot.models.chat import Chat


class ChatRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(context="testing")
        self.client = self.app.test_client()

        self.chat1 = Chat(title="some title")
        self.chat2 = Chat(title="some other title")

    @patch("feathr_bot.routes.chat.ChatService")
    def test_create_endpoint(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.create_initial_chat.return_value = {
            "id": 1,
            "messages": [
                {"role": "system", "content": "some content"},
                {"role": "user", "content": "some content"},
                {"role": "assistant", "content": "some content"},
            ],
            "title": "some title",
        }

        response = self.client.post("/chat/", json={"message": "some text"})

        self.assertEqual(response.status_code, HTTPStatus.OK)

        mock_service.assert_called_once_with(
            data={"message": "some text", "sassy": False}
        )
        mock_instance.create_initial_chat.assert_called_once()

    @patch("feathr_bot.routes.chat.ChatService")
    def test_list_endpoint(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.get_all.return_value = [self.chat1, self.chat2]

        response = self.client.get("/chat/")

        self.assertEqual(response.status_code, HTTPStatus.OK)

        mock_service.assert_called_once()
        mock_instance.get_all.assert_called_once()

    @patch("feathr_bot.routes.chat.ChatService")
    def test_get_endpoint(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.find_by_id.return_value = self.chat1

        response = self.client.get("/chat/1/")

        self.assertEqual(response.status_code, HTTPStatus.OK)

        mock_service.assert_called_once()
        mock_instance.find_by_id.assert_called_once_with(chat_id=1)

    @patch("feathr_bot.routes.chat.ChatService")
    def test_get_endpoint(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.find_by_id.return_value = self.chat1

        response = self.client.get("/chat/1/")

        self.assertEqual(response.status_code, HTTPStatus.OK)

        mock_service.assert_called_once()
        mock_instance.find_by_id.assert_called_once_with(chat_id=1)

    @patch("feathr_bot.routes.chat.ChatService")
    def test_create_chat_message_endpoint(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.create_chat_message.return_value = {
            "id": 1,
            "messages": [
                {"role": "system", "content": "some content"},
                {"role": "user", "content": "some content"},
                {"role": "assistant", "content": "some content"},
                {"role": "user", "content": "some more content"},
                {"role": "assistant", "content": "mo content"},
            ],
            "title": "some title",
        }

        response = self.client.post("/chat/1/message", json={"message": "some text"})

        self.assertEqual(response.status_code, HTTPStatus.OK)

        mock_service.assert_called_once_with(
            data={"message": "some text", "sassy": False}
        )
        mock_instance.create_chat_message.assert_called_once()
