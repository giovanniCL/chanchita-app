from domain.user_domain import UserDomain
from presentation.requests.login_request import LoginRequest
from presentation.responses.generic_response import Response
from presentation.responses.login_response import LoginResponse

class UserApplication:
    def __init__(self) -> None:
        self.domain = UserDomain()

    def login(self, data: LoginRequest) -> Response:
        try:
            login_response_data = self.domain.login(
                username=data.username,
                password=data.password
            )
            return LoginResponse(200, "Login succesful", login_response_data)
        except ValueError as e:
            print(e)
            return Response(code=400, message=str(e))
        except Exception as e:
            print(e)
            return Response(code=500, message="INTERNAL ERROR")

    def register(self, data: LoginRequest) -> Response:
        try:
            register_response_data = self.domain.register(
                username=data.username,
                password=data.password
            )
            return LoginResponse(200, "Register succesful", register_response_data)
        except ValueError as e:
            print(e)
            return Response(code=400, message=str(e))
        except Exception as e:
            print(e)
            return Response(code=500, message="INTERNAL ERROR")

