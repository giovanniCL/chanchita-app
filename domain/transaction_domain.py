from infrastructure.repositories import Repositories
from typing import List
from .entities.transaction import Transaction
from .entities.balance import Balance

class TransactionDomain:
    def __init__(self) -> None:
        self.repository = Repositories.TRANSACTION_REPOSITORY
        self.balance_repository = Repositories.BALANCE_REPOSITORY
        self.membership_repository = Repositories.MEMBERSHIP_REPOSITORY

    def validate_creditor(self, username: str, membership_id: str) -> None:
        membership = self.membership_repository.get_membership(membership_id)
        if not membership:
            raise PermissionError("Miembro no existe")
        if membership.user_id != username:
            raise PermissionError("Usuario no tiene permiso para realizar transacción")
        
    def validate_debtors(self, debtor_ids: List[str], creditor_id: str) -> None:
        debtors = self.membership_repository.get_memberships(debtor_ids)
        if len(debtors) != len(debtor_ids):
            raise ValueError("Uno o más deudores no existen")
        group_id_set = set([debtor.group_id for debtor in debtors])
        if len(group_id_set) == 0:
            raise ValueError("Deudores no existen")
        if len(group_id_set) > 1:
            raise PermissionError("Deudores no pertenecen al mismo grupo")
        creditor = self.membership_repository.get_membership(creditor_id)
        if creditor.group_id != group_id_set.get():
            raise PermissionError("Creditor y deudores no pertenecen al mismo grupo")

    def make_payment(
            self,
            amount: float,
            description: str,
            creditor: str,
            debtors: List[str],
            username: str
    ) -> Transaction:
        payment = Transaction(
            type="PAYMENT",
            amount=amount,
            description=description,
            creditor=creditor
        )
        self.validate_creditor(username, creditor)
        self.validate_debtors(debtors, creditor)
        self.repository.add_transaction(payment)
        debt_amount = amount / len(debtors)
        debts = [
            Balance(
                type="DEBT",
                amount=-debt_amount,
                member=debtor,
                transaction=payment.uuid
            ) for debtor in debtors
        ]
        credit = Balance(
            type="CREDIT",
            amount=amount,
            member=creditor,
            transaction=payment.uuid
        )
        self.balance_repository.add_balances([credit, *debts])
        return payment

        
        