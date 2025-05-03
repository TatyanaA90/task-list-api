from flask import Blueprint,abort, make_response, request, Response
from app.models.task import Task
from app.routes.helpers import validate_model, create_new_model_dict
from ..db import db


bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@bp.post("")
def create_task():
    request_body = request.get_json()

    return create_new_model_dict(Task,request_body)
