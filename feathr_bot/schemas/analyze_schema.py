from marshmallow import fields, Schema


class AnalyzeRequestSchema(Schema):
    """Class for Analyze request schema"""

    prompt = fields.Str(required=True)


class AnalyzeResponseSchema(Schema):
    """Class for Analyze response schema"""

    result = fields.Str(dump_only=True)
