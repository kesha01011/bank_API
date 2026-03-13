from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.deposit_fixture import DepositFixture
from src.main.api.db.crud.transaction_crud import TransactionCrudDB as Transaction
from sqlalchemy.orm import Session


import pytest

@pytest.mark.api
class TestUserDeposit:
    def test_deposit(self, api_manager: ApiManager, deposit_user_request:DepositFixture, db_session: Session):
        response = api_manager.user_steps.deposit_user(deposit_user_request.user, deposit_user_request.request)
        assert response.balance == deposit_user_request.request.amount

        transaction_from_db = Transaction.get_transaction_by_account_id(db_session, deposit_user_request.request.accountId)
        assert transaction_from_db.amount == deposit_user_request.request.amount, 'Транзакция не найдена в БД'

    def test_deposit_invalid(self, api_manager: ApiManager, deposit_user_request:DepositFixture):
        deposit_user_request.request.amount = 9001
        api_manager.user_steps.deposit_invalid_user(deposit_user_request.user, deposit_user_request.request)