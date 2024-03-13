from dataclasses import dataclass

from src.planner.movements.application.responses import MovementResponse


@dataclass(frozen=True)
class FindMovementQuery:
    RESPONSE = MovementResponse
    id: str
    account_owner_id: str
