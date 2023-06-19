from marshmallow import fields, Schema


class MessageSchema(Schema):
    """Class for Message schema"""

    role = fields.Str(required=True)
    content = fields.Str(required=True)
