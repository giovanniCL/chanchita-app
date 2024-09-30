from .sql_alchemy_base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, ForeignKey, String
from .user_repository import UserRepository
from .group_repository import GroupRepository
from domain.entities.group import Group
from domain.entities.membership import Membership
from typing import Self, List


class MembershipRepository(Base):
    __tablename__ = "membership"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    uuid = mapped_column(String(50), unique=True)
    name = mapped_column(String(50), nullable=True)
    user_id = mapped_column(String(), ForeignKey("user.username"), nullable=True)
    group_id = mapped_column(String(), ForeignKey("group.uuid"))

    @classmethod
    def add(cls, membership: Membership) -> None:
        with cls.client.session() as session:
            new_record = cls.from_entity(membership)
            session.add(new_record)
            session.commit()

    @classmethod
    def get_membership(cls, membership_id: str) -> Membership | None:
        with cls.client.session() as session:
            membership = session.query(
                MembershipRepository
            ).filter(
                MembershipRepository.uuid == membership_id
            ).first()
        if not membership: return None
        return membership.to_entity()
        
    @classmethod
    def get_memberships(cls, membership_ids: List[str]) -> List[Membership]:
        with cls.client.session() as session:
            memberships = session.query(
                cls.id.in_(membership_ids)
            ).all()
        return [membership.to_entity() for membership in memberships]


    @classmethod
    def get_groups(cls, username: str):
        with cls.client.session() as session:
            user = session.query(
                UserRepository
                ).filter(
                    UserRepository.username == username
                ).first()
        if not user: return []
        return [Group(name=group.name, uuid=group.uuid) for group in user.groups]
        
    def to_entity(self) -> Membership:
        return Membership(
            name=self.name,
            uuid=self.uuid,
            user_id=self.user_id,
            group_id=self.group_id
        )

    @classmethod
    def from_entity(cls, entity: Membership) -> Self:
        return cls(
            user_id=entity.user_id,
            group_id=entity.group_id,
            name=entity.name,
            uuid=entity.uuid
        )
            
