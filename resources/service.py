from flask_restful import Resource
from flask import request





class Service(Resource):
    @classmethod
    def get(cls, id: int):
        return { "id": id }


class ServiceList(Resource):
    @classmethod
    def get(cls):
        pass