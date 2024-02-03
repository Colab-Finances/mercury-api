from dataclasses import dataclass

from src.planner.accounts.domain.value_objects.currency import Currency


@dataclass(frozen=True)
class AccountResponse:
    id: str
    user_id: str
    name: str
    currency: Currency
    balance: int
