from dataclasses import dataclass
from enum import Enum
from typing import List, Self, Union

from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.movements.domain.transfers.aggregate import TransferMovement


class MovementType(Enum):
    EXPENSE = "expense"
    INCOME = "income"
    TRANSFER = "transfer"


@dataclass(frozen=True)
class ExpenseMovementResponse:
    account_id: str
    amount: int
    date: str
    id: str
    type: MovementType

    @classmethod
    def from_entity(cls, expense: ExpenseMovement) -> Self:
        return cls(
            account_id=expense.account_id.primitive,
            amount=expense.amount.primitive,
            date=expense.date.primitive,
            id=expense.id.primitive,
            type=MovementType.EXPENSE,
        )


@dataclass(frozen=True)
class IncomeMovementResponse:
    account_id: str
    amount: int
    date: str
    id: str
    type: MovementType

    @classmethod
    def from_entity(cls, income: IncomeMovement) -> Self:
        return cls(
            account_id=income.account_id.primitive,
            amount=income.amount.primitive,
            date=income.date.primitive,
            id=income.id.primitive,
            type=MovementType.INCOME,
        )


@dataclass(frozen=True)
class TransferMovementResponse:
    amount: int
    date: str
    destination_id: str
    id: str
    origin_id: str
    type: MovementType

    @classmethod
    def from_entity(cls, transfer: TransferMovement) -> Self:
        return cls(
            destination_id=transfer.destination_id.primitive,
            origin_id=transfer.origin_id.primitive,
            amount=transfer.amount.primitive,
            date=transfer.date.primitive,
            id=transfer.id.primitive,
            type=MovementType.TRANSFER,
        )


MovementResponse = Union[
    ExpenseMovementResponse, IncomeMovementResponse, TransferMovementResponse
]


@dataclass(frozen=True)
class MovementsResponse:
    data: List[MovementResponse]
