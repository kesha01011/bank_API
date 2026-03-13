from src.main.api.models.base_model import BaseModel


class CreditRequestUserRequest(BaseModel):

    accountId: int
    amount: int
    termMonths: int
