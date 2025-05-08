from flask import Blueprint,abort, make_response, request, Response
from app.models.goal import Goal
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
