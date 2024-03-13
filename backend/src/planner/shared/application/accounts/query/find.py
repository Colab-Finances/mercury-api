from dataclasses import dataclass

from src.planner.shared.application.accounts.response import AccountResponse


@dataclass(frozen=True)
class FindAccountQuery:
    RESPONSE = AccountResponse
    id: str
    owner_id: str
