import uuid
from infrastructure.repositories import Repositories
from .entities.group import Group
from .entities.membership import Membership
from typing import List

class GroupDomain:
    def __init__(self) -> None:
        self.repository = Repositories.GROUP_REPOSITORY
        self.membership_repository = Repositories.MEMBERSHIP_REPOSITORY

    def create_group(self, name: str, username: str) -> Group:
        group = Group(name=name, uuid=str(uuid.uuid4()))
        self.repository.add_group(group)
        self.membership_repository.add(
            Membership(
                user_id=username,
                group_id=group.uuid,
                name=username
            )
        )
        return group
    
    def get_groups(self, username: str) -> List[Group]:
        groups = self.membership_repository.get_groups(username)
        return groups
    
    def join_group(self, group_id: str, username: str,) -> Group:
        self.membership_repository.add(
            Membership(
                user_id=username,
                group_id=group_id,
                name=username
            )
        )
        group = self.repository.get_group(group_id)
        return group

