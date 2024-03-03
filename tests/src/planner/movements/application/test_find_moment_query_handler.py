from unittest.mock import Mock

import pytest

from src.planner.movements.application.find.finder import MovementFinder
from src.planner.movements.application.find.query import FindMovementQuery
from src.planner.movements.application.find.query_handler import (
    FindMovementQueryHandler,
)
from src.planner.movements.application.responses import (
    ExpenseMovementResponse,
    IncomeMovementResponse,
    TransferMovementResponse,
)
from src.planner.movements.domain.exceptions.not_found import MovementNotFound
from src.planner.movements.domain.repository import MovementRepository
from src.planner.shared.domain.exceptions.base import DomainException
from tests.src.planner.movements.factories import (
    ExpenseMovementFactory,
    IncomeMovementFactory,
    TransferMovementFactory,
)

pytestmark = pytest.mark.anyio


class TestFindMovementQueryHandler:
    def setup_method(self) -> None:
        # Mocks
        self._repository = Mock(spec=MovementRepository)

        use_case = MovementFinder(self._repository)
        self.handler = FindMovementQueryHandler(use_case)

    async def test_should_return_an_expense(self) -> None:
        expense = ExpenseMovementFactory.build()
        query = FindMovementQuery(
            account_owner_id=expense.account_owner_id.primitive, id=expense.id.primitive
        )

        self._repository.search.return_value = expense

        response = await self.handler(query)
        assert isinstance(response, ExpenseMovementResponse)

        self._repository.search.assert_called_once_with(expense.id)

    async def test_should_return_an_income(self) -> None:
        income = IncomeMovementFactory.build()
        query = FindMovementQuery(
            account_owner_id=income.account_owner_id.primitive, id=income.id.primitive
        )
        self._repository.search.return_value = income

        response = await self.handler(query)
        assert isinstance(response, IncomeMovementResponse)

        self._repository.search.assert_called_once_with(income.id)

    async def test_should_return_a_transfer(self) -> None:
        transfer = TransferMovementFactory.build()
        query = FindMovementQuery(
            account_owner_id=transfer.account_owner_id.primitive,
            id=transfer.id.primitive,
        )
        self._repository.search.return_value = transfer

        response = await self.handler(query)
        assert isinstance(response, TransferMovementResponse)

        self._repository.search.assert_called_once_with(transfer.id)

    async def test_should_raise_error_not_found_if_account_belong_to_another_user(
        self, faker
    ) -> None:
        expense = ExpenseMovementFactory.build()
        query = FindMovementQuery(
            id=expense.id.primitive, account_owner_id=faker.uuid4()
        )

        with pytest.raises(MovementNotFound) as excinfo:
            await self.handler(query)

        self._repository.search.assert_called_once_with(expense.id)

        assert isinstance(excinfo.value, DomainException)
        assert excinfo.value.message == "Movement not found."
        assert excinfo.value.code == 404
