from dataclasses import dataclass


@dataclass(frozen=True)
class MovementResponse:
    type: str
    id: str
    amount: str
    date: str


class ExpenseMovementResponse(MovementResponse):
    account_id: str


class IncomeMovementResponse(MovementResponse):
    account_id: str


class TransferMovementResponse(MovementResponse):
    origin_id: str
    destination_id: str
