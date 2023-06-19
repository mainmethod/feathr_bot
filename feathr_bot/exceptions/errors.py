from http import HTTPStatus


class FeathrBotError(Exception):
    """Base class for FeathrBot API errors"""

    status = HTTPStatus.INTERNAL_SERVER_ERROR
    code = "api_error"
    description = "An API error has occured"

    def __init__(self, code=None, description=None, status=None):
        if code:
            self.code = code
        if description:
            self.description = description
        if status:
            self.status = status


class FeathrBotSqlAlchemyError(FeathrBotError):
    code = "database_error"

    def __init__(self, description="a database error occurred"):
        self.description = description


class FeathrBotChatServiceError(FeathrBotError):
    code = "service_error"
    status = HTTPStatus.UNPROCESSABLE_ENTITY

    def __init__(self, description="an chat service error occurred"):
        self.description = description


class FeathrBotNotFoundError(FeathrBotError):
    code = "database_error"
    status = HTTPStatus.NOT_FOUND

    def __init__(self, description="Resource not found"):
        self.description = description
