from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from config import HOST, PORT, DB, USER, PASSWORD, ENGINE
def create_sqlite_connection() -> Engine:
    return create_engine(f'sqlite:///db1.db')


def create_postgres_connection() -> Engine:
    return create_engine(
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    )


ENGINE_MAPPING = {
    "sqlite": create_sqlite_connection,
    "postgres": create_postgres_connection
}

class SqlAlchemyClient:
    def __init__(self):
        self.engine = ENGINE_MAPPING[ENGINE]()
        self.session = sessionmaker(bind=self.engine)