from flask import Blueprint
from http import HTTPStatus
from webargs.flaskparser import use_args
from flask_cors import cross_origin

from feathr_bot.schemas.analyze_schema import (
    AnalyzeRequestSchema,
    AnalyzeResponseSchema,
)
from feathr_bot.services.analyze_service import AnalyzeService

blueprint = Blueprint("analyze_blueprint", __name__, url_prefix="/analyze")


@blueprint.route("/", methods=("POST",))
@cross_origin()
@use_args(AnalyzeRequestSchema)
def create(args):
    """Analyze some text"""
    prompt = args.get("prompt")
    result = AnalyzeService(prompt=prompt).analyze()
    return AnalyzeResponseSchema().dump({"result": result}), HTTPStatus.OK
