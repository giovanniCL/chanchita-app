from .generic_response_data import GenericResponseData
from dataclasses import dataclass

@dataclass
class LoginResponseData(GenericResponseData):
    authentication_token: str