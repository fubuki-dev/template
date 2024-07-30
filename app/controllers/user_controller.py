from fubuki import Controller, route
from app.models.user import User
import json

class UserController(Controller):
    @route("/users")
    async def index(scope, receive, send):
        users = User.get_all()
        response = {
            "status": 200,
            "body": users
        }
        return response

    @route("/users/create", methods=["POST"])
    async def create(scope, receive, send):
        try:
            body = await receive()
            data = json.loads(body["body"].decode("utf-8"))
            user = User.create(data)
            response = {
                "status": 201,
                "body": {
                    "message": "User created",
                    "user": user
                }
            }
        except Exception as e:
            response = {
                "status": 400,
                "body": {"message": str(e)}
            }
        return response