from flask import Blueprint, request
from application.group_application import GroupApplication
from .requests.groups.create_group_request import CreateGroupRequest
from .requests.authorized_request import AuthorizedRequest
from .requests.groups.join_group_request import JoinGroupRequest

group_application = GroupApplication()

group_blueprint = Blueprint('group_blueprint', __name__)

@group_blueprint.route('/create', methods=["POST"])
def create_group():
    authorization = request.headers.get("Authorization")
    body = request.get_json()
    create_group_request = CreateGroupRequest(authorization=authorization,**body)
    create_group_response = group_application.create_group(create_group_request)
    return create_group_response.to_dict(), create_group_response.code

@group_blueprint.route('/', methods=["GET"])
def get_groups():
    authorization = request.headers.get("Authorization")
    get_groups_request = AuthorizedRequest(authorization=authorization)
    get_groups_response = group_application.get_groups(get_groups_request)
    return get_groups_response.to_dict(), get_groups_response.code

@group_blueprint.route('/join', methods=["POST"])
def join_group():
    authorization = request.headers.get("Authorization")
    body = request.get_json()
    join_group_request = JoinGroupRequest(authorization=authorization, **body)
    join_group_response = group_application.join_group(join_group_request)
    return join_group_response.to_dict(), join_group_response.code
