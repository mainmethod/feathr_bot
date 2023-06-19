from flask import Blueprint
from http import HTTPStatus
from webargs.flaskparser import use_args
from feathr_bot.schemas.chat_schema import ChatRequestSchema, ChatResponseSchema
from feathr_bot.services.chat_service import ChatService
from flask_cors import cross_origin

blueprint = Blueprint("chat_blueprint", __name__, url_prefix="/chat")


@blueprint.route("/", methods=("POST", "OPTIONS"))
@cross_origin()
@use_args(ChatRequestSchema)
def create(args):
    """Start a chat"""
    chat = ChatService(data=args).create_initial_chat()
    return ChatResponseSchema().dump(chat), HTTPStatus.OK


@blueprint.route("/", methods=("GET", "OPTIONS"))
@cross_origin()
def list():
    """Get all chats"""
    chats = ChatService().get_all()
    return ChatResponseSchema(many=True).dump(chats), HTTPStatus.OK


@blueprint.route("/<int:chat_id>/", methods=("GET", "OPTIONS"))
@cross_origin()
def get(chat_id):
    """Get single chat by id"""
    chat = ChatService().find_by_id(chat_id=chat_id)
    return ChatResponseSchema().dump(chat), HTTPStatus.OK


@blueprint.route("/<int:chat_id>/message", methods=("POST", "OPTIONS"))
@cross_origin()
@use_args(ChatRequestSchema)
def create_chat_message(args, chat_id):
    """Add new message to chat"""
    chat = ChatService(data=args).create_chat_message(chat_id=chat_id)
    return ChatResponseSchema().dump(chat), HTTPStatus.OK
