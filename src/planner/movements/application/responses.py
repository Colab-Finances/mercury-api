from dataclasses import dataclass, field
from enum import Enum
from typing import Union


class MovementType(Enum):
    EXPENSE = "expense"
    INCOME = "income"
    TRANSFER = "transfer"


@dataclass(frozen=True)
class ExpenseMovementResponse:
    account_id: str
    amount: str
    date: str
    id: str
    type: MovementType = field(default=MovementType.EXPENSE, init=False)


@dataclass(frozen=True)
class IncomeMovementResponse:
    account_id: str
    amount: str
    date: str
    id: str
    type: MovementType = field(default=MovementType.INCOME, init=False)


@dataclass(frozen=True)
class TransferMovementResponse:
    amount: str
    date: str
    destination_id: str
    id: str
    origin_id: str
    type: MovementType = field(default=MovementType.TRANSFER, init=False)


MovementResponse = Union[
    ExpenseMovementResponse, IncomeMovementResponse, TransferMovementResponse
]
