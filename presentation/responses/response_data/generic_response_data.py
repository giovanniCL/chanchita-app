from dataclasses import dataclass, asdict

@dataclass
class GenericResponseData:
    def to_dict(self) -> dict:
        return asdict(self)