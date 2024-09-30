from .sql_alchemy_base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, ForeignKey, Float
from ..typing.sqlalchemy_types import ChoiceType
from domain.entities.transaction import Transaction

class TransactionRepository(Base):
    __tablename__ = "transaction"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    uuid = mapped_column(String(), unique=True)
    type = mapped_column(ChoiceType({"PAYMENT": "PAYMENT", "REFUND": "REFUND"}))
    amount = mapped_column(Float())
    description = mapped_column(String(100), nullable=True)
    creditor_id = mapped_column(String(), ForeignKey("membership.uuid"))

    def add_transaction(self, transaction: Transaction) -> None:
        with self.client.session() as session:
            new_transaction = TransactionRepository(
                uuid=transaction.uuid,
                type=transaction.type,
                amount=transaction.amount,
                description=transaction.description,
                creditor_id=transaction.creditor
            )
            session.add(new_transaction)
            session.commit()
