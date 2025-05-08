from flask import abort, make_response
from ..db import db
import os
import requests

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = { "details": "Invalid data" } 
        abort(make_response(response , 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        response = {"details": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))
    
    return model

def create_new_model_dict(cls, model_data):

    try:
        new_instance = cls.from_dict(model_data)

    except KeyError as error:
        response = { "details": "Invalid data" } 
        abort(make_response(response, 400))

    db.session.add(new_instance)
    db.session.commit()

    response = new_instance.to_dict()
    return {f"{cls.__name__}".lower(): response}, 201


def send_slack_message(message):
    url = os.environ.get("SLACK_URI")
    slack_token = os.environ.get("SLACK_TOKEN")
    slack_chanel_id = os.environ.get("SLACK_CHANEL_ID")

    token = f"Bearer {slack_token}"
    headers = {"Content-type": "application/json", "Authorization": token}
    request_body = { "channel": slack_chanel_id, "text": message}

    requests.post(url, json=request_body, headers=headers)
