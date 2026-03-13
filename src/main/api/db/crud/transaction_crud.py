from src.main.api.db.models.transaction_table import Transaction
from sqlalchemy.orm import Session


class TransactionCrudDB:
    @staticmethod
    def get_transaction_by_account_id(db: Session, to_account_id: int) -> Transaction | None:
        return db.query(Transaction).filter_by(to_account_id = to_account_id).first()
