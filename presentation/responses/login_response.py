from .generic_response import Response
from .response_data.login_response_data import LoginResponseData

class LoginResponse(Response):
    data: LoginResponseData