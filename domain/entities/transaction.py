from dataclasses import dataclass
from .uuid_entity import UUIDEntity
@dataclass
class Transaction(UUIDEntity):
    type: str
    amount: float
    description: str
    creditor: str