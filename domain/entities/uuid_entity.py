import uuid
from dataclasses import dataclass, field

@dataclass
class UUIDEntity:
    def create_uuid():
        return str(uuid.uuid4())
    
    uuid: str = field(default_factory=create_uuid)

