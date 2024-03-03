from kink import inject

from src.planner.movements.application.mappers import entity_to_response
from src.planner.movements.application.responses import MovementResponse
from src.planner.movements.domain.value_objects import MovementId
from src.planner.shared.domain.users import UserId

from .finder import MovementFinder
from .query import FindMovementQuery


@inject
class FindMovementQueryHandler:
    QUERY = FindMovementQuery

    def __init__(self, use_case: MovementFinder) -> None:
        self.use_case = use_case

    async def __call__(self, query: FindMovementQuery) -> MovementResponse:
        movement = await self.use_case(
            id=MovementId(query.id), account_owner_id=UserId(query.account_owner_id)
        )
        return entity_to_response(movement)
