from flask_restful import Resource

INVALID_CREDENTIALS = "Invalid credentials!"


class UserLogin(Resource):
    @classmethod
    def post(cls):
        return {"message": INVALID_CREDENTIALS}, 401
