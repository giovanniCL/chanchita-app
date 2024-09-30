from .sql_alchemy_base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, Float, ForeignKey
from ..typing.sqlalchemy_types import ChoiceType
from domain.entities.balance import Balance
from typing import List

class BalanceRepository(Base):
    __tablename__ = "balance"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    type = mapped_column(ChoiceType({"DEBIT": "DEBIT", "CREDIT": "CREDIT"}))
    amount = mapped_column(Float())
    transaction_id = mapped_column(Integer(), ForeignKey("transaction.id"))
    membership_id = mapped_column(Integer(), ForeignKey("membership.id"))

    def add_balances(self, balances: List[Balance]) -> None:
        with self.client.session() as session:
            new_balances = [
                BalanceRepository(
                type=balance.type,
                amount=balance.amount,
                transaction_id=balance.transaction,
                membership_id = balance.member
                ) for balance in balances
            ]
            session.add_all(new_balances)
            session.commit()


