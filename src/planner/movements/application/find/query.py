from dataclasses import dataclass


@dataclass(frozen=True)
class FindMovementQuery:
    id: str
    account_owner_id: str
