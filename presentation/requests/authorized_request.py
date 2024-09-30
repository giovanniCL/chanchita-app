from pydantic import BaseModel

class AuthorizedRequest(BaseModel):
    authorization: str