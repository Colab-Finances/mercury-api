import pytest
from kink import di
from sqlalchemy.ext.asyncio import AsyncSession

from src.planner.accounts.domain.repository import AccountRepository
from src.planner.movements.domain.repository import MovementRepository
from src.planner.movements.infrastructure.repositories.sqlalchemy import (
    SqlAlchemyMovementRepository,
)
from src.planner.users.domain.repository import UserRepository
from tests.src.planner.movements.factories import ExpenseMovementFactory
from tests.src.planner.shared.factories.accounts import AccountFactory
from tests.src.planner.users.factories import UserFactory

pytestmark = pytest.mark.anyio


@pytest.mark.skip(reason="Deprecate Repository")
class TestSqlAlchemyMovementRepository:
    def setup_method(self):
        self.user = UserFactory.build()
        self.account = AccountFactory.build(owner_id=self.user.id.primitive)
        self.expense = ExpenseMovementFactory.build(
            account_id=self.account.id.primitive
        )

    def test_should_be_a_valid_repository(self):
        assert issubclass(SqlAlchemyMovementRepository, MovementRepository)

    async def test_should_create_a_movement(
        self, sqlalchemy_sessionmaker: type[AsyncSession]
    ):
        repository = SqlAlchemyMovementRepository(sqlalchemy_sessionmaker)
        await di[UserRepository].save(self.user)  # type:ignore [type-abstract]
        await di[AccountRepository].save(self.account)  # type:ignore [type-abstract]

        await repository.save(self.expense)

    async def test_should_not_return_a_non_existing_expense(
        self, sqlalchemy_sessionmaker: type[AsyncSession]
    ):
        repository = SqlAlchemyMovementRepository(sqlalchemy_sessionmaker)

        assert await repository.search(self.expense.id) is None

    async def test_should_return_an_expense_by_id(
        self, sqlalchemy_sessionmaker: type[AsyncSession]
    ):
        repository = SqlAlchemyMovementRepository(sqlalchemy_sessionmaker)
        await di[UserRepository].save(self.user)  # type:ignore [type-abstract]
        await di[AccountRepository].save(self.account)  # type:ignore [type-abstract]

        await repository.save(self.expense)
        perssisted_expense = await repository.search(self.expense.id)
        assert self.expense == perssisted_expense
