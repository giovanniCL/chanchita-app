from flask import Blueprint, request
from application.user_application import UserApplication
from .requests.login_request import LoginRequest

user_application = UserApplication()

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/login', methods=["POST"])
def login():
    body = request.get_json()
    login_request = LoginRequest(**body)
    login_response = user_application.login(login_request)
    return login_response.to_dict(), login_response.code

@user_blueprint.route('/register', methods=["POST"])
def register():
    body = request.get_json()
    register_request = LoginRequest(**body)
    register_response = user_application.register(register_request)
    return register_response.to_dict(), register_response.code