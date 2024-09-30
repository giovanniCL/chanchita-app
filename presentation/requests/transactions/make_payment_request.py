from ..authorized_request import AuthorizedRequest
from typing import List

class MakePaymentRequest(AuthorizedRequest):
    amount: float
    description: str
    creditor: str
    debtors: List[str]

