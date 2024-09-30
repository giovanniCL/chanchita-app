from ..authorized_request import AuthorizedRequest

class CreateGroupRequest(AuthorizedRequest):
    name: str
