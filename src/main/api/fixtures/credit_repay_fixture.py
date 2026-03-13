import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.fixtures.user_fixture import create_credit_user_request
from src.main.api.models.credit_request_user_request import CreditRequestUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest


class CreditRepayFixture:
    user : CreateCreditUserRequest
    request: CreditRepayRequest
    def __init__(self, user: CreateCreditUserRequest, request: CreditRepayRequest):
        self.user = user
        self.request = request

@pytest.fixture
def credit_repay_user_request(api_manager: ApiManager, create_credit_user_request: CreateCreditUserRequest):
    user = create_credit_user_request
    response_account = api_manager.user_steps.create_account(user)
    credit_request = CreditRequestUserRequest(accountId=response_account.id, amount=5000, termMonths=12)
    response_credit = api_manager.user_steps.credit_request_user(user, credit_request)
    request = CreditRepayRequest(creditId=response_credit.creditId, accountId=response_credit.id,amount=5000)
    return CreditRepayFixture(user, request)
