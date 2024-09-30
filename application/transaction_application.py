from domain.transaction_domain import TransactionDomain
from .utils.decorators import authentication_required
from presentation.responses.generic_response import Response
from presentation.requests.transactions.make_payment_request import MakePaymentRequest

class TransactionApplication:
    def __init__(self) -> None:
        self.domain = TransactionDomain()

    @authentication_required
    def make_payment(self, request: MakePaymentRequest, username: str) -> Response:
        try:
            payment = self.domain.make_payment(
                amount=request.amount,
                description=request.description,
                creditor=request.creditor,
                debtors=request.debtors,
                username=username
            )
            return Response(code=201, message=f"Pago exitoso")
        except ValueError as e:
            print(e)
            return Response(code=400, message=str(e))
        except PermissionError as e:
            print(e)
            return Response(code=403, message=str(e))
        except Exception as e:
            print(e)
            return Response(code=500, message="INTERNAL ERROR")