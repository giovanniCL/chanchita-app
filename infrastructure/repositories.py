from .sqlalchemy_repositories import (
    BalanceRepository,
    UserRepository,
    TransactionRepository,
    GroupRepository,
    MembershipRepository
)

class Repositories:
    BALANCE_REPOSITORY = BalanceRepository
    USER_REPOSITORY = UserRepository
    TRANSACTION_REPOSITORY = TransactionRepository
    GROUP_REPOSITORY = GroupRepository
    MEMBERSHIP_REPOSITORY = MembershipRepository

    @classmethod
    def init_tables(cls):
        cls.USER_REPOSITORY.init_tables()
