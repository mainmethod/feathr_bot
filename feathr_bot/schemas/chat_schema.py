from marshmallow import fields, Schema


class ChatRequestSchema(Schema):
    """Class for Chat request schema"""

    message = fields.Str(required=True)
    sassy = fields.Bool(missing=False)


class ChatResponseSchema(Schema):
    """Class for Chat response schema"""

    id = fields.Int(dump_only=True)
    title = fields.Str(dump_only=True)
    messages = fields.Nested("MessageSchema", dump_only=True, many=True)
