from requests import Response
from src.main.api.models.transfer_user_request import TransferUserRequest
from src.main.api.models.transfer_user_response import TransferUserResponse
from src.main.api.requests.requester import Requester
import requests

class TransferUserRequester(Requester):
    def post(self, transfer_user_request: TransferUserRequest) -> TransferUserResponse | Response:
        url=f"{self.base_url}/account/transfer"
        response = requests.post(
            url=url,
            json=transfer_user_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return TransferUserResponse(**response.json())