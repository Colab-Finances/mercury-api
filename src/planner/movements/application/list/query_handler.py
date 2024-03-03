from typing import List
from kink import inject

from src.planner.movements.application.mappers import entity_to_response
from src.planner.movements.application.responses import MovementsResponse
from src.planner.shared.domain.users import UserId

from .lister import MovementLister
from .query import ListMovementQuery


@inject
class ListMovementQueryHandler:
    QUERY = ListMovementQuery

    def __init__(self, use_case: MovementLister) -> None:
        self.use_case = use_case

    async def __call__(self, query: ListMovementQuery) -> MovementsResponse:
        movements = await self.use_case(account_owner_id=UserId(query.account_owner_id))
        return MovementsResponse(
            data=[entity_to_response(movement) for movement in movements]
        )
