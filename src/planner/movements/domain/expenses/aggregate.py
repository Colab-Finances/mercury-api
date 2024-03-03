from dataclasses import dataclass
from re import U
from typing import Self

from src.planner.movements.domain.aggregate import Movement
from src.planner.movements.domain.value_objects.amount import MovementAmount
from src.planner.movements.domain.value_objects.date import MovementDate
from src.planner.movements.domain.value_objects.id import MovementId
from src.planner.shared.domain.accounts import AccountId
from src.planner.shared.domain.movements.events import ExpenseMovementAdded
from src.planner.shared.domain.users.id import UserId


@dataclass
class ExpenseMovement(Movement):
    account_id: AccountId

    @classmethod
    def add(
        cls,
        id: MovementId,
        amount: MovementAmount,
        account_id: AccountId,
        date: MovementDate,
        account_owner_id: UserId,
    ) -> Self:
        expense = cls(id=id, amount=amount, account_id=account_id, date=date, account_owner_id=account_owner_id)
        expense._record_event(
            ExpenseMovementAdded.make(
                expense.id.primitive,
                date=expense.date.primitive,
                amount=expense.amount.primitive,
                account_id=expense.account_id.primitive,
                account_owner_id=expense.account_owner_id.primitive,
            )
        )
        return expense
