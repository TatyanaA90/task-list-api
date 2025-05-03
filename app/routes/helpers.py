from flask import abort, make_response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = { "details": "Invalid data" } #{"message": f"{cls.__title__} {model_id} invalid" }
        abort(make_response(response , 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        response = { "details": "Invalid data" } #{"message": f"{cls.__title__} {model_id} not found"}
        abort(make_response(response, 404))
    
    return model

def create_new_model_dict(cls, data):

    try:
        new_instance = cls.from_dict(data)

    except KeyError as error:
        response = { "details": "Invalid data" } #{"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_instance)
    db.session.commit()

    response = new_instance.to_dict()
    return {"task":response}, 201

