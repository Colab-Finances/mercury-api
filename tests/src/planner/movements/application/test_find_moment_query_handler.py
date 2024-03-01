from unittest.mock import Mock

import pytest

from src.planner.movements.application.find.finder import MovementFinder
from src.planner.movements.application.find.query import FindMovementQuery
from src.planner.movements.application.find.query_handler import (
    FindMovementQueryHandler,
)
from src.planner.movements.domain.exceptions import MovementNotFound
from src.planner.movements.domain.repository import MovementRepository
from src.planner.shared.domain.exceptions.base import DomainException
from src.shared.domain.bus.event.event_bus import EventBus
from tests.src.planner.movements.factories import (
    ExpenseMovementFactory,
    IncomeMovementFactory,
    TransferMovementFactory,
)
from tests.src.planner.shared.factories.accounts import AccountFactory

pytestmark = pytest.mark.anyio


class TestFindMovementQueryHandler:
    def setup_method(self) -> None:
        # Mocks
        self._repository = Mock(spec=MovementRepository)
        self._event_bus = Mock(EventBus)

        use_case = MovementFinder(self._repository, self._event_bus)
        self.handler = FindMovementQueryHandler(use_case)

        # Arrange
        self.account = AccountFactory.build()

    async def test_should_return_an_expense(self) -> None:
        expense = ExpenseMovementFactory.build(account_id=self.account.id.primitive)
        query = FindMovementQuery.from_dict(
            user_id=self.account.owner_id.primitive, id=expense.id.primitive
        )

        await self.handler(query)

        self._repository.find.assert_called_once_with(self.expense.id)

    async def test_should_return_an_income(self) -> None:
        income = IncomeMovementFactory.build(account_id=self.account.id.primitive)
        query = FindMovementQuery.from_dict(
            user_id=self.account.owner_id.primitive, id=income.id.primitive
        )

        await self.handler(query)

        self._repository.find.assert_called_once_with(self.income.id)

    async def test_should_return_a_transfer(self) -> None:
        transfer = TransferMovementFactory.build(account_id=self.account.id.primitive)
        query = FindMovementQuery.from_dict(
            user_id=self.account.owner_id.primitive, id=transfer.id.primitive
        )

        await self.handler(query)

        self._repository.find.assert_called_once_with(self.transfer.id)

    async def test_should_raise_error_not_found_if_account_belong_to_another_user(
        self, faker
    ) -> None:
        expense = ExpenseMovementFactory.build(account_id=self.account.id.primitive)
        query = FindMovementQuery.from_dict(
            id=expense.id.primitive, user_id=faker.uuid4()
        )

        with pytest.raises(MovementNotFound) as excinfo:
            await self.handler(query)

        self._repository.find.assert_called_once_with(self.expense.id)

        assert isinstance(excinfo.value, DomainException)
        assert excinfo.value.message == "Movement not found"
        assert excinfo.value.code == 404
