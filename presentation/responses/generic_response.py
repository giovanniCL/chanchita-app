from dataclasses import dataclass, asdict
from .response_data.generic_response_data import GenericResponseData

@dataclass
class Response:
    code: int
    message: str
    data: GenericResponseData = None

    def to_dict(self) -> dict:
        return asdict(self)