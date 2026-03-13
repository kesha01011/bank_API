from src.main.api.models.base_model import BaseModel
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule

class DepositUserRequest(BaseModel):
    accountId: int
    amount: Annotated[int, CreationRule(regex=r'^ (?:[1-8][0-9]{3} | 9000)$')]