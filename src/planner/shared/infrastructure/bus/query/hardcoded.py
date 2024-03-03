from kink import inject

from src.planner.accounts.application.find.query_handler import FindAccountQueryHandler
from src.planner.auth_token.application.find.query import FindAuthTokenQuery
from src.planner.auth_token.application.find.query_handler import (
    FindAuthTokenQueryHandler,
)
from src.planner.movements.application.find.query_handler import (
    FindMovementQueryHandler,
)
from src.planner.shared.application.accounts.query import FindAccountQuery
from src.planner.shared.domain.bus.query import Query, QueryBus, QueryResponse
from src.planner.shared.domain.bus.query.exceptions import QueryNotRegistered
from src.planner.users.application.find.query import FindUserQuery
from src.planner.users.application.find.query_handler import FindUserQueryHandler


@inject(alias=QueryBus)
class HardcodedQueryBus:
    HANDLERS = {
        FindUserQuery: FindUserQueryHandler,
        FindAuthTokenQuery: FindAuthTokenQueryHandler,
        FindAccountQuery: FindAccountQueryHandler,
        FindMovementQueryHandler.QUERY: FindMovementQueryHandler,
    }

    async def ask(self, command: Query) -> QueryResponse:
        try:
            return await self.HANDLERS[command.__class__]()(command)
        except KeyError:
            raise QueryNotRegistered(command)
