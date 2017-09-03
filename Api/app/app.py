from flask import Flask, jsonify

app = Flask(__name__)

from app.models import Sprint


@app.route('/get_all')
def hello_world():
    # from flask_sqlalchemy import SQLAlchemy
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5011'
    # db = SQLAlchemy(app)
    # db.init_app(app)

    return jsonify([p.to_dict() for p in Sprint.query.all()])


@app.route('/create', methods=['POST'])
def create():
    from flask import request
    json = request.get_json()
    p = Sprint(**json)
    p.save()
    return jsonify(p.to_dict())
