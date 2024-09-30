from dataclasses import dataclass
from .uuid_entity import UUIDEntity

@dataclass
class Membership(UUIDEntity):
    name: str
    user_id: str
    group_id: str