from unittest.mock import Mock
from uuid import uuid4

import pytest

from src.planner.movements.application.list.lister import MovementLister
from src.planner.movements.application.list.query_handler import (
    ListMovementQueryHandler,
)
from src.planner.movements.application.responses import (
    ExpenseMovementResponse,
    IncomeMovementResponse,
    MovementsResponse,
    TransferMovementResponse,
)
from src.planner.movements.domain.repository import MovementRepository
from src.planner.shared.domain.users.id import UserId
from tests.src.planner.movements.factories import (
    ExpenseMovementFactory,
    IncomeMovementFactory,
    TransferMovementFactory,
)

pytestmark = pytest.mark.anyio


class TestListMovementQueryHandler:
    def setup_method(self) -> None:
        self._repository = Mock(spec=MovementRepository)

        use_case = MovementLister(self._repository)
        self.handler = ListMovementQueryHandler(use_case)
        self.account_owner_id = str(uuid4())

    async def test_should_return_a_list_of_movements(self) -> None:
        expense = ExpenseMovementFactory.build(account_owner_id=self.account_owner_id)
        income = IncomeMovementFactory.build(account_owner_id=self.account_owner_id)
        transfer = TransferMovementFactory.build(account_owner_id=self.account_owner_id)
        query = self.handler.QUERY(
            account_owner_id=self.account_owner_id,
        )

        self._repository.match.return_value = [expense, income, transfer]

        response = await self.handler(query)
        assert isinstance(response, MovementsResponse)
        assert response.data == [
            ExpenseMovementResponse.from_entity(expense),
            IncomeMovementResponse.from_entity(income),
            TransferMovementResponse.from_entity(transfer),
        ]

        self._repository.match.assert_called_once_with(UserId(self.account_owner_id))

    async def test_should_return_a_empty_list_of_movements(self) -> None:
        query = self.handler.QUERY(
            account_owner_id=self.account_owner_id,
        )

        response = await self.handler(query)
        assert isinstance(response, MovementsResponse)
        assert response.data == []
        self._repository.match.assert_called_once_with(UserId(self.account_owner_id))
