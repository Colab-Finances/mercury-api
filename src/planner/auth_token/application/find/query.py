from dataclasses import dataclass
from typing import Optional

from src.planner.auth_token.application.shared.response import AuthTokenResponse


@dataclass(frozen=True)
class FindAuthTokenQuery:
    access_token: Optional[str]

    class Response(AuthTokenResponse):
        pass
