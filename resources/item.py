from flask_restful import Resource
from flask import request
from models.item import ItemModel
from schemas.item import ItemSchema

ERROR_INSERTING = "An error occurred while inserting the item."
ITEM_NOT_FOUND = "Item not found."

item_schema = ItemSchema()


class Item(Resource):
    @classmethod
    def get(cls, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            return item_schema.dump(item)
        return {"message": ITEM_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if ItemModel.find_by_name(name):
            return {"message": "'{}' already exists".format(name)}, 400

        item_json = request.get_json()
        item_json["name"] = name

        item = item_schema.load(item_json)
        item.save_to_db()


        return item_schema.dump(item), 201
