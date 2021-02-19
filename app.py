from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.user import UserLogin
from resources.item import Item
from resources.service import Service, ServiceList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validator(err):
    return jsonify(err), 400


api = Api(app)
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ServiceList, "/services")
api.add_resource(Service, "/service/<int:id>")
api.add_resource(UserLogin, "/login")

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
