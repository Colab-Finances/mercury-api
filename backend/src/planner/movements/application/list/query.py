from dataclasses import dataclass
from typing import Optional

from src.planner.movements.application.responses import MovementsResponse


@dataclass(frozen=True)
class ListMovementQuery:
    RESPONSE = MovementsResponse
    account_owner_id: str
    from_date: Optional[str] = None
    to_date: Optional[str] = None
