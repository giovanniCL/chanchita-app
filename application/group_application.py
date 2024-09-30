from domain.group_domain import GroupDomain
from presentation.requests.groups.create_group_request import CreateGroupRequest
from presentation.requests.authorized_request import AuthorizedRequest
from presentation.requests.groups.join_group_request import JoinGroupRequest
from presentation.responses.generic_response import Response
from presentation.responses.group_list_response import GroupListResponse, GroupListResponseData
from typing import List
from .utils.decorators import authentication_required

class GroupApplication:
    def __init__(self) -> None:
        self.domain = GroupDomain()

    @authentication_required
    def create_group(self, request: CreateGroupRequest, username: str) -> Response:
        try:
            group = self.domain.create_group(request.name, username=username)
            return Response(code=201, message= f"Group {group.name} created succesfully with uuid: {group.uuid}")
        except PermissionError as e:
            print(e)
            return Response(code=403, message=str(e))
        except Exception as e:
            print(e)
            return Response(code=500, message="INTERNAL ERROR")
        
    @authentication_required
    def get_groups(self, request:AuthorizedRequest, username: str) -> Response:
        try:
            groups = self.domain.get_groups(username=username)
            groups_data = [GroupListResponseData(name=group.name) for group in groups]
            return GroupListResponse(code=200, message="", data=groups_data)
        except PermissionError as e:
            print(e)
            return Response(code=403, message=str(e))
        except Exception as e:
            print(e)
            return Response(code=500, message="INTERNAL ERROR")
        
    @authentication_required
    def join_group(self, request: JoinGroupRequest, username: str) -> Response:
        try:
            group = self.domain.join_group(request.group_id, username=username)
            return Response(code=200, message=f"Succesfully joined {group.name}")
        except PermissionError as e:
            print(e)
            return Response(code=403, message=str(e))
        except Exception as e:
            print(e)
            return Response(code=500, message="INTERNAL ERROR")
        

