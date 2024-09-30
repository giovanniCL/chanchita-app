from .sql_alchemy_base import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String, Integer
from domain.entities.group import Group


class GroupRepository(Base):
    __tablename__ = "group"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    uuid = mapped_column(String(36), unique=True)
    name = mapped_column(String(50))
    members = relationship("UserRepository", secondary="membership", back_populates="groups")

    @classmethod
    def add_group(cls, group: Group) -> None:
        with cls.client.session() as session:
            new_group = cls(name=group.name, uuid=group.uuid)
            session.add(new_group)
            session.commit()

    @classmethod
    def get_group(cls, group_id: str) -> Group:
        with cls.client.session() as session:
            result = session.query(cls).filter(cls.uuid == group_id).first()
        if not result: return None
        return Group(name=result.name, uuid=result.uuid)

    