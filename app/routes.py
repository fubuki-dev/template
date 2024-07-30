from app.controllers.home_controller import HomeController
from app.controllers.user_controller import UserController

def setup_routes(app):
    for controller_class in [HomeController, UserController]:
        app.add_route(controller_class)