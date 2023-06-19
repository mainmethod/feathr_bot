from flask import Blueprint, jsonify
from http import HTTPStatus
from feathr_bot.exceptions.errors import FeathrBotError
from werkzeug.exceptions import HTTPException

blueprint = Blueprint("errors", __name__)


@blueprint.app_errorhandler(FeathrBotError)
def handle_api_error(e):
    """Handle App-specific errors"""
    return (
        jsonify({"code": e.code, "description": e.description, "status": e.status}),
        e.status,
    )


@blueprint.app_errorhandler(Exception)
def handle_error(e):
    """Handle http and unhandled exceptions"""
    status = HTTPStatus.INTERNAL_SERVER_ERROR
    if isinstance(e, HTTPException):
        status = e.code
    return (
        jsonify(
            {"code": "unhandled_exception", "description": str(e), "status": status}
        ),
        status,
    )
