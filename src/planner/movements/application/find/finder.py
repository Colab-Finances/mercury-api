from kink import inject

from src.planner.movements.domain.aggregate import Movement
from src.planner.movements.domain.exceptions.not_found import MovementNotFound
from src.planner.movements.domain.repository import MovementRepository
from src.planner.movements.domain.value_objects import MovementId
from src.planner.shared.domain.users import UserId


@inject(use_factory=True)
class MovementFinder:
    def __init__(self, repository: MovementRepository):
        self._repository = repository

    async def __call__(self, id: MovementId, account_owner_id: UserId) -> Movement:
        movement = await self._repository.search(id)
        if not movement or movement.account_owner_id != account_owner_id:
            raise MovementNotFound

        return movement
