from feathr_bot.exceptions.errors import (
    FeathrBotSqlAlchemyError,
    FeathrBotChatServiceError,
    FeathrBotNotFoundError,
)
from feathr_bot.models.chat import Chat
from feathr_bot.models.message import Message
from feathr_bot.schemas.message_schema import MessageSchema
from feathr_bot.services.openai_service import OpenAIService

DEFAULT_CONTENT = "Act like you are a really nice, and thoughful support engineer replying to general tech questions."
SASSY_CONTENT = "Act like you are a sassy support engineer responding to general tech questions.  Please make all responses very sassy."


class ChatService(object):
    """Class to handle Chat-related services"""

    def __init__(self, data: dict = {}) -> None:
        self.data = data

    def create_initial_chat(self) -> Chat:
        """create initial chat"""
        message = self.data.get("message")
        sassy = self.data.get("sassy")
        try:
            new_chat = Chat(title=message)
            chat = new_chat.save()

            content = SASSY_CONTENT if sassy else DEFAULT_CONTENT

            default_message = Message(
                role="system",
                content=content,
            )
            chat.messages.append(default_message)

            new_message = Message(role="user", content=message)
            chat.messages.append(new_message)

            service = OpenAIService()
            response = service.chat(
                messages=MessageSchema(many=True).dump(chat.messages)
            )

            data = MessageSchema().load(response["choices"][0]["message"])
            final_message = Message(**data)
            chat.messages.append(final_message)
            return chat.save()
        except FeathrBotSqlAlchemyError as e:
            raise FeathrBotChatServiceError from e

    def create_chat_message(self, chat_id: int) -> Chat:
        """create a chat message"""
        message = self.data.get("message")
        try:
            chat = Chat.query.get(chat_id)

            new_message = Message(role="user", content=message)
            chat.messages.append(new_message)

            service = OpenAIService()
            response = service.chat(
                messages=MessageSchema(many=True).dump(chat.messages)
            )

            data = MessageSchema().load(response["choices"][0]["message"])
            final_message = Message(**data)
            chat.messages.append(final_message)
            return chat.save()
        except FeathrBotSqlAlchemyError as e:
            raise FeathrBotChatServiceError from e

    def find_by_id(self, chat_id: int) -> Chat:
        """get a single chat"""
        if chat := Chat.query.get(chat_id):
            return chat
        else:
            raise FeathrBotNotFoundError

    def get_all(self) -> list[Chat]:
        """get all chats"""
        return Chat.query.order_by(Chat.created_on.desc()).all()
