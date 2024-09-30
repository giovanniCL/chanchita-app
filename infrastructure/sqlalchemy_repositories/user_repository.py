from .sql_alchemy_base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, relationship
from domain.entities.user import User

class UserRepository(Base):
    __tablename__ = "user"
    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    username = mapped_column(String(50), unique=True)
    password = mapped_column(String())
    groups = relationship("GroupRepository", secondary="membership", back_populates="members")

    @classmethod
    def get_user_from_username(cls, username: str) -> User | None:
        with cls.client.session() as session:
            result = session.query(
                UserRepository
            ).filter(
                UserRepository.username == username
            ).first()
        if not result: return None
        return User(
            username=result.username,
            password=result.password
        )
        
    @classmethod
    def add_user(cls, user: User) -> None:
        with cls.client.session() as session:
            new_user = UserRepository(username=user.username, password=user.password)
            session.add(new_user)
            session.commit()

