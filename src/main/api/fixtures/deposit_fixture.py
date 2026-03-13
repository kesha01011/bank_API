import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.fixtures.user_fixture import create_user_request
from src.main.api.models.deposit_user_request import DepositUserRequest


class DepositFixture:
    user : CreateUserRequest
    request: DepositUserRequest
    def __init__(self, user: CreateUserRequest, request: DepositUserRequest):
        self.user = user
        self.request = request

@pytest.fixture
def deposit_user_request(api_manager: ApiManager, create_user_request: CreateUserRequest):
    user = create_user_request
    response_account = api_manager.user_steps.create_account(create_user_request)
    generated_request = RandomModelGenerator.generate(DepositUserRequest)
    request = DepositUserRequest(accountId=response_account.id, amount=generated_request.amount)

    return DepositFixture(user, request)


