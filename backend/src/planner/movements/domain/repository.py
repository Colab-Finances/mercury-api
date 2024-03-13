from typing import List, Optional, Protocol, Union, runtime_checkable

from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.movements.domain.transfers.aggregate import TransferMovement
from src.planner.movements.domain.value_objects.id import MovementId
from src.planner.shared.domain.users.id import UserId

from .aggregate import Movement

MovementType = Union[ExpenseMovement, IncomeMovement, TransferMovement]


@runtime_checkable
class MovementRepository(Protocol):
    # TODO: Use save in other repositories
    async def save(self, movement: Movement) -> None:
        ...

    async def search(self, id: MovementId) -> Optional[MovementType]:
        ...

    async def match(self, account_owner_id: UserId) -> List[MovementType]:
        ...
