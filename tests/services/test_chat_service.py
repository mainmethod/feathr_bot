import mock
import unittest
from feathr_bot.services.chat_service import ChatService
from feathr_bot.exceptions.errors import (
    FeathrBotChatServiceError,
    FeathrBotSqlAlchemyError,
)

from feathr_bot.app import create_app
from feathr_bot.extensions import db
from feathr_bot.models.chat import Chat


class ChatServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @mock.patch("feathr_bot.services.chat_service.OpenAIService.chat")
    def test_create_initial_chat(self, mock_chat) -> None:
        mock_return_value = {
            "choices": [{"message": {"role": "assistant", "content": "some response"}}]
        }
        mock_chat.return_value = mock_return_value

        chat = ChatService({"message": "some message"}).create_initial_chat()

        mock_chat.assert_called_once()

        assert len(chat.messages) == 3

    @mock.patch("feathr_bot.services.chat_service.OpenAIService.chat")
    @mock.patch("feathr_bot.services.chat_service.Chat.save")
    def test_create_initial_chat_raises(self, mock_chat, mock_chat_save) -> None:
        mock_chat_save.side_effect = FeathrBotSqlAlchemyError

        with self.assertRaises(FeathrBotChatServiceError) as e:
            ChatService({"message": "some message"}).create_initial_chat()

            mock_chat.assert_not_called()

    @mock.patch("feathr_bot.services.chat_service.OpenAIService.chat")
    def test_create_chat_message(self, mock_chat) -> None:
        chat = Chat(title="some title")
        chat.save()

        mock_return_value = {
            "choices": [{"message": {"role": "assistant", "content": "some response"}}]
        }
        mock_chat.return_value = mock_return_value

        chat = ChatService({"message": "some message"}).create_chat_message(1)

        mock_chat.assert_called_once()

        assert len(chat.messages) == 2
