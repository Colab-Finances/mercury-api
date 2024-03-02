from dataclasses import dataclass


class MovementResponse:
    type: str
    id: str
    amount: str
    date: str


@dataclass(frozen=True)
class ExpenseMovementResponse(MovementResponse):
    account_id: str


@dataclass(frozen=True)
class IncomeMovementResponse(MovementResponse):
    account_id: str


@dataclass(frozen=True)
class TransferMovementResponse(MovementResponse):
    origin_id: str
    destination_id: str
