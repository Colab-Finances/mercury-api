from dataclasses import dataclass


@dataclass(frozen=True)
class FindMovementQuery:
    id: str
    owner_id: str
