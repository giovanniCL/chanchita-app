from domain.user_domain import UserDomain
from typing import Callable

USER_DOMAIN = UserDomain()

def authentication_required(func: Callable) -> Callable:
    def wrapper(*args,**kwargs):
        request = args[1]
        auth = request.authorization
        username = USER_DOMAIN.authorize(auth)
        if not username:
            raise PermissionError("No esta autenticado")
        return func(*args, username, **kwargs)
    return wrapper
