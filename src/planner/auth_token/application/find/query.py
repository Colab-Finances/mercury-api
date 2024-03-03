from dataclasses import dataclass
from typing import Optional

from src.planner.auth_token.application.shared.response import AuthTokenResponse


@dataclass(frozen=True)
class FindAuthTokenQuery:
    RESPONSE = AuthTokenResponse
    access_token: Optional[str]
