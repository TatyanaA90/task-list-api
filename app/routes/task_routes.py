from flask import Blueprint,abort, make_response, request, Response
from app.models.task import Task
from app.routes.helpers import validate_model, create_new_model_dict
from ..db import db


bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@bp.post("")
def create_task():
    request_body = request.get_json()

    return create_new_model_dict(Task,request_body)

@bp.get("")
def get_all_task():
    query = db.select(Task)

    title_param = request.args.get("title")
    if title_param:
        query = query.where(Task.title.ilike(f"%{title_param}%"))

    description_param = request.args.get("description")
    if title_param:
        query = query.where(Task.description.ilike(f"%{description_param}%"))

    is_complete_param = request.args.get("is_complete")
    if title_param:
        query = query.where(Task.completed_at.ilike(f"%{is_complete_param}%"))

    tasks = db.session.scalars(query.order_by(Task.id))

    tasks_response = []
    for task in tasks:
        tasks_response.append(task.to_dict())
        
    return tasks_response


