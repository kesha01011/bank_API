from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.transfer_fixture import TransferFixture
from src.main.api.db.crud.transaction_crud import TransactionCrudDB as Transaction
from sqlalchemy.orm import Session
import pytest

@pytest.mark.api
class TestUserTransfer:
    def test_transfer(self,db_session:Session, api_manager:ApiManager, transfer_user_request:TransferFixture):
        response = api_manager.user_steps.transfer_user(transfer_user_request.userFrom, transfer_user_request.request)
        expected_balance = transfer_user_request.depositAmount - transfer_user_request.request.amount
        assert response.fromAccountIdBalance == expected_balance

        transaction_from_db = Transaction.get_transaction_by_account_id(db_session, transfer_user_request.request.toAccountId)
        assert transaction_from_db.amount == transfer_user_request.request.amount, 'Транзакция не найдена в БД'

    def test_deposit_invalid(self, api_manager:ApiManager, transfer_user_request:TransferFixture):
        transfer_user_request.request.amount = 499
        api_manager.user_steps.transfer_invalid_user(transfer_user_request.userFrom, transfer_user_request.request)