from .generic_response import Response
from .response_data.group_list_response_data import GroupListResponseData
from typing import List


class GroupListResponse(Response):
    data: List[GroupListResponseData]