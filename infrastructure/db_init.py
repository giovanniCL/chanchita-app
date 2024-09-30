from infrastructure.repositories import Repositories
def db_init() -> None:
    Repositories.CLIENT.init_tables()