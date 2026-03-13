import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.fixtures.user_fixture import create_credit_user_request
from src.main.api.models.credit_request_user_request import CreditRequestUserRequest


class CreditFixture:
    user : CreateCreditUserRequest
    request: CreditRequestUserRequest
    def __init__(self, user: CreateCreditUserRequest, request: CreditRequestUserRequest):
        self.user = user
        self.request = request

@pytest.fixture
def credit_request_user_request(api_manager: ApiManager, create_credit_user_request: CreateCreditUserRequest):
    user = create_credit_user_request
    response_account = api_manager.user_steps.create_account(user)
    request = CreditRequestUserRequest(accountId=response_account.id, amount=5000, termMonths=12)
    return CreditFixture(user, request)

