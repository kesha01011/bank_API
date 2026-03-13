from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.credit_repay_fixture import CreditRepayFixture
from src.main.api.db.crud.credit_crud import CreditCrudDB as Credit
from sqlalchemy.orm import Session
import pytest

@pytest.mark.api
class TestUserCreditRepay:
    def test_credit_repay(self,db_session:Session, api_manager: ApiManager, credit_repay_user_request:CreditRepayFixture):
        response = api_manager.user_steps.credit_repay_user(credit_repay_user_request.user, credit_repay_user_request.request)

        assert response.amountDeposited == credit_repay_user_request.request.amount
        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)
        assert credit_from_db.balance == 0, 'Кредит не найден в БД'

    def test_invalid_credit_repay(self, api_manager: ApiManager, credit_repay_user_request:CreditRepayFixture):
        credit_repay_user_request.request.amount = 2000
        api_manager.user_steps.credit_invalid_repay_user(credit_repay_user_request.user, credit_repay_user_request.request)