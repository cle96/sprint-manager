from flask import Flask, jsonify, abort
from sqlalchemy import exc

app = Flask(__name__)

from app.models import Sprint


@app.route('/get_all')
def hello_world():
    return jsonify([p.to_dict() for p in Sprint.query.all()])


@app.route('/create', methods=['POST'])
def create():
    from flask import request
    json = request.get_json()
    s = Sprint(**json)
    try:
        s.save()
    except exc.SQLAlchemyError:
        s.rollback()
        abort(404)
    return jsonify(s.to_dict())
