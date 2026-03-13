from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.credit_request_fixture import CreditFixture
from src.main.api.db.crud.credit_crud import CreditCrudDB as Credit
from sqlalchemy.orm import Session
import pytest

@pytest.mark.api
class TestUserCreditRequest:
    def test_credit_request(self, db_session: Session, api_manager: ApiManager, credit_request_user_request:CreditFixture):
        response = api_manager.user_steps.credit_request_user(credit_request_user_request.user, credit_request_user_request.request)

        assert response.balance == credit_request_user_request.request.amount
        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)
        assert credit_from_db.amount == credit_request_user_request.request.amount, 'Кредит не найден в БД'

    def test_credit_invalid(self, api_manager: ApiManager, credit_request_user_request:CreditFixture):
        credit_request_user_request.request.amount = 2000
        api_manager.user_steps.credit_invalid_request_user(credit_request_user_request.user, credit_request_user_request.request)