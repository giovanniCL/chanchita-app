from flask import Blueprint, request
from application.transaction_application import TransactionApplication
from .requests.transactions.make_payment_request import MakePaymentRequest

transaction_application = TransactionApplication()

transaction_blueprint = Blueprint('transaction_blueprint', __name__)

@transaction_blueprint.route('/payment', methods=["POST"])
def make_payment():
    authorization = request.headers.get("Authorization")
    body = request.get_json()
    payment_request = MakePaymentRequest(authorization=authorization, **body)
    payment_response = transaction_application.make_payment(payment_request)
    return payment_response.to_dict(), payment_response.code
