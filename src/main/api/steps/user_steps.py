from src.main.api.foundation import endpoint
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request_user_request import CreditRequestUserRequest
from src.main.api.models.deposit_user_request import DepositUserRequest
from src.main.api.models.transfer_user_request import TransferUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def deposit_user(self, user: CreateUserRequest, request: DepositUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.DEPOSIT_USER,
            ResponseSpecs.request_ok()
        ).post(request)
        return response

    def deposit_invalid_user(self, user: CreateUserRequest, request: DepositUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.DEPOSIT_USER,
            ResponseSpecs.request_bad()
        ).post(request)

    def transfer_user(self, user: CreateUserRequest, request: TransferUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.TRANSFER_USER,
            ResponseSpecs.request_ok()
        ).post(request)
        return response

    def transfer_invalid_user(self, user: CreateUserRequest, request: TransferUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.TRANSFER_USER,
            ResponseSpecs.request_bad()
        ).post(request)

    def credit_request_user(self, user: CreateUserRequest, request: CreditRequestUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_created()
        ).post(request)
        return response

    def credit_invalid_request_user(self, user: CreateUserRequest, request: CreditRequestUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_bad()
        ).post(request)

    def credit_repay_user(self, user: CreateUserRequest, request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_ok()
        ).post(request)
        return response

    def credit_invalid_repay_user(self, user: CreateUserRequest, request: CreditRepayRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=user.username, password=user.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_Unprocessable()
        ).post(request)