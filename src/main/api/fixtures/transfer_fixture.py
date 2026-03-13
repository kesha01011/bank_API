import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.fixtures.user_fixture import create_user_request
from src.main.api.models.transfer_user_request import TransferUserRequest
from src.main.api.models.deposit_user_request import DepositUserRequest


class TransferFixture:
    userFrom: CreateUserRequest
    userTo: CreateUserRequest
    request: TransferUserRequest

    def __init__(self, userFrom : CreateUserRequest, userTo : CreateUserRequest, request: TransferUserRequest, depositAmount: float ):
        self.userFrom  = userFrom
        self.userTo = userTo
        self.request = request
        self.depositAmount = depositAmount

@pytest.fixture
def transfer_user_request(api_manager: ApiManager, create_user_request:CreateUserRequest):
    userFrom = create_user_request
    userTo = CreateUserRequest(
        username=f"{userFrom.username[:13]}to",
        password=userFrom.password,
        role=userFrom.role
    )
    api_manager.admin_steps.create_user(userTo)

    response_account_from = api_manager.user_steps.create_account(userFrom)
    response_account_to = api_manager.user_steps.create_account(userTo)

    generated_request = RandomModelGenerator.generate(DepositUserRequest)
    deposit_amount = generated_request.amount

    deposit_request = DepositUserRequest(accountId=response_account_from.id, amount=generated_request.amount)

    api_manager.user_steps.deposit_user(userFrom, deposit_request)

    request = TransferUserRequest(fromAccountId=response_account_from.id, toAccountId=response_account_to.id,amount=899.5)

    return TransferFixture(userFrom, userTo, request, deposit_amount)