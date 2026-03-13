from requests import Response
from src.main.api.models.credit_request_user_request import CreditRequestUserRequest
from src.main.api.models.credit_request_user_response import CreditRequestUserResponse
from src.main.api.requests.requester import Requester
import requests

class CreditRequestUserRequester(Requester):
    def post(self, credit_request_user_request: CreditRequestUserRequest) -> CreditRequestUserResponse | Response:
        url=f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json=credit_request_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return CreditRequestUserResponse(**response.json())