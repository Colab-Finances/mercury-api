from typing import List, Union

from kink import inject

from src.planner.movements.domain.repository import MovementRepository, MovementType
from src.planner.shared.domain.users import UserId


@inject(use_factory=True)
class MovementLister:
    def __init__(self, repository: MovementRepository):
        self._repository = repository

    async def __call__(self, account_owner_id: UserId) -> List[MovementType]:
        return await self._repository.match(account_owner_id)
