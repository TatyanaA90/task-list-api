from flask import Blueprint,abort, make_response, request, Response
from app.models.goal import Goal
from app.models.task import Task
from app.routes.helpers import validate_model, create_new_model_dict, send_slack_message
from ..db import db


bp = Blueprint("goal_bp", __name__, url_prefix="/goals")

@bp.post("")
def create_goal():
    request_body = request.get_json()

    return create_new_model_dict(Goal,request_body)


@bp.get("")
def get_all_goal():
    query = db.select(Goal)

    title_param = request.args.get("title")
    if title_param:
        query = query.where(Goal.title.ilike(f"%{title_param}%"))

    goals = db.session.scalars(query.order_by(Goal.id))

    goals_response = [goal.to_dict() for goal in goals]
        
    return goals_response



@bp.get("/<id>")
def get_one_goal(id):
    goal = validate_model(Goal, id)
        
    return  {"goal": goal.to_dict()}



@bp.put("/<id>")
def update_goal(id):
    goal = validate_model(Goal, id)
    request_body = request.get_json()

    goal.update_from_dict(request_body)

    db.session.commit()

    return Response(status=204, mimetype="application/json")



@bp.delete("/<id>")
def delete_goal(id):
    goal = validate_model(Goal, id)
    db.session.delete(goal)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.post("/<id>/tasks")
def assign_tasks_to_goal(id):
    goal = validate_model(Goal, id)

    request_body = request.get_json()
    task_ids = request_body.get("task_ids")

    tasks = []
    for task_id in task_ids:
        task = validate_model(Task, task_id)
        tasks.append(task)
        # task.goal_id = id
    goal.tasks = tasks
    db.session.commit()

    return {"id": goal.id, "task_ids": task_ids}

@bp.get("/<id>/tasks")
def get_tasks_by_goal(id):
    goal = validate_model(Goal, id)

    return goal.to_dict_with_tasks()
