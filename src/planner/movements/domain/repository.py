from typing import Optional, Protocol, Union, runtime_checkable

from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.movements.domain.transfers.aggregate import TransferMovement
from src.planner.movements.domain.value_objects.id import MovementId

from .aggregate import Movement

MovementType = Union[ExpenseMovement, IncomeMovement, TransferMovement]


@runtime_checkable
class MovementRepository(Protocol):
    # TODO: Use save in other repositories
    async def save(self, movement: Movement) -> None:
        ...

    async def search(self, id: MovementId) -> Optional[MovementType]:
        ...
