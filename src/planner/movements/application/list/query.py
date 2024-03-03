from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ListMovementQuery:
    account_owner_id: str
    from_date: Optional[str] = None
    to_date: Optional[str] = None
