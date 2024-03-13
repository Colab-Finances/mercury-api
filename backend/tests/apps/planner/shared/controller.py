from fastapi import status
from httpx import Response


class TestController:
    def ensure_return_unauthorized_missing_token(
        self,
        response: Response,
    ) -> None:
        assert response.status_code == status.HTTP_401_UNAUTHORIZED, response.text

        json_response = response.json()
        assert len(json_response["detail"]) == 1
        error_response = json_response["detail"][0]
        assert error_response["msg"] == "Is required"
        assert error_response["source"] == "access_token"
