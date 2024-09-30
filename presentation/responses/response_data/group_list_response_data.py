from dataclasses import dataclass
from .generic_response_data import GenericResponseData

@dataclass
class GroupListResponseData(GenericResponseData):
    name: str