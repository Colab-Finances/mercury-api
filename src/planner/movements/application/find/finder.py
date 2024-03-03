from typing import Union

from kink import inject

from src.planner.movements.domain.exceptions.not_found import MovementNotFound
from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.movements.domain.repository import MovementRepository, MovementType
from src.planner.movements.domain.transfers.aggregate import TransferMovement
from src.planner.movements.domain.value_objects import MovementId
from src.planner.shared.domain.users import UserId


@inject(use_factory=True)
class MovementFinder:
    def __init__(self, repository: MovementRepository):
        self._repository = repository

    async def __call__(self, id: MovementId, account_owner_id: UserId) -> MovementType:
        movement = await self._repository.search(id)
        if not movement or movement.account_owner_id != account_owner_id:
            raise MovementNotFound

        return movement
