from dataclasses import asdict, dataclass

from src.planner.movements.application.incomes.add.command import (
    AddIncomeMovementCommand,
)
from dataclasses import asdict, dataclass

from src.planner.movements.application.expenses.add.command import (
    AddExpenseMovementCommand,
)

from src.planner.movements.application.transfers.add.command import (
    AddTransferMovementCommand,
)


@dataclass(frozen=True)
class AddTransferSchema:
    __annotations__ = {
        key: value
        for key, value in AddTransferMovementCommand.__annotations__.items()
        if key not in ["id", "user_id"]
    }

    def to_dict(self):
        return asdict(self)


@dataclass(frozen=True)
class AddIncomeSchema:
    __annotations__ = {
        key: value
        for key, value in AddIncomeMovementCommand.__annotations__.items()
        if key not in ["id", "user_id"]
    }

    def to_dict(self):
        return asdict(self)


@dataclass(frozen=True)
class AddExpenseSchema:
    __annotations__ = {
        key: value
        for key, value in AddExpenseMovementCommand.__annotations__.items()
        if key not in ["id", "user_id"]
    }

    def to_dict(self):
        return asdict(self)
