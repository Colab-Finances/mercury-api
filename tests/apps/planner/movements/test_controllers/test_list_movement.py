from unittest.mock import ANY

import pytest
from faker import Faker
from fastapi import status
from httpx import AsyncClient
from kink import di
from motor.core import AgnosticDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from apps.planner.backend.config import settings
from src.planner.movements.domain.repository import MovementRepository
from src.planner.users.domain.repository import UserRepository
from tests.apps.planner.shared.auth import AuthAsUser
from tests.apps.planner.shared.controller import TestController
from tests.src.planner.movements.factories import TransferMovementFactory
from tests.src.planner.movements.factories.expenses import ExpenseMovementFactory
from tests.src.planner.movements.factories.incomes import IncomeMovementFactory
from tests.src.planner.users.factories import UserFactory

fake = Faker()

pytestmark = pytest.mark.anyio


class TestListMovementController(TestController):
    def setup_method(self):
        self._user = UserFactory.build()
        self._url = f"{settings.API_PREFIX}/v1/movements"

    async def test_should_return_a_list_of_movements(
        self,
        client: AsyncClient,
        sqlalchemy_sessionmaker: type[AsyncSession],
        motor_database: AgnosticDatabase,
    ) -> None:
        await di[UserRepository].save(self._user)  # type: ignore[type-abstract]
        transfer = TransferMovementFactory.build(
            account_owner_id=self._user.id.primitive
        )
        expense = ExpenseMovementFactory.build(account_owner_id=self._user.id.primitive)
        income = IncomeMovementFactory.build(account_owner_id=self._user.id.primitive)
        await di[MovementRepository].save(transfer)  # type: ignore[type-abstract]
        await di[MovementRepository].save(expense)  # type: ignore[type-abstract]
        await di[MovementRepository].save(income)  # type: ignore[type-abstract]

        response = await client.get(self._url, auth=AuthAsUser(self._user.id))

        assert response.status_code == status.HTTP_200_OK, response.text
        json_response = response.json()
        assert json_response == {"data": ANY}
        assert len(json_response["data"]) == 3
        assert json_response["data"] == [
            {
                "id": transfer.id.primitive,
                "amount": transfer.amount.primitive,
                "date": transfer.date.primitive,
                "origin_id": transfer.origin_id.primitive,
                "destination_id": transfer.destination_id.primitive,
                "type": "transfer",
            },
            {
                "id": income.id.primitive,
                "amount": income.amount.primitive,
                "date": income.date.primitive,
                "account_id": income.account_id.primitive,
                "type": "income",
            },
            {
                "id": expense.id.primitive,
                "amount": expense.amount.primitive,
                "date": expense.date.primitive,
                "account_id": expense.account_id.primitive,
                "type": "expense",
            },
        ]

    async def test_should_return_unauthorized_missing_token(
        self,
        client: AsyncClient,
        sqlalchemy_sessionmaker: type[AsyncSession],
        motor_database: AgnosticDatabase,
    ) -> None:
        self.ensure_return_unauthorized_missing_token(
            await client.get(self._url % fake.uuid4())
        )
