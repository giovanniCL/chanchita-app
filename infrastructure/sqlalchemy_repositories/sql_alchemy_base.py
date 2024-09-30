from sqlalchemy.orm import DeclarativeBase
from .sql_alchemy_client import SqlAlchemyClient
class Base(DeclarativeBase):
    client = SqlAlchemyClient()

    @classmethod
    def init_tables(cls):
        cls.metadata.create_all(bind=cls.client.engine)