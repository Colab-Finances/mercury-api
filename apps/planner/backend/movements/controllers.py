from typing import Annotated, cast

from fastapi import Depends
from kink import di

from apps.planner.backend.shared.auth import oauth2_scheme
from src.planner.auth_token.application.find.query import FindAuthTokenQuery
from src.planner.auth_token.application.shared.response import AuthTokenResponse
from src.planner.movements.application.incomes.add.command import (
    AddIncomeMovementCommand,
)
from src.planner.movements.application.transfers.add.command import (
    AddTransferMovementCommand,
)
from src.planner.shared.domain.bus.command import CommandBus
from src.planner.shared.domain.bus.query import QueryBus
from src.planner.movements.application.expenses.add.command import (
    AddExpenseMovementCommand,
)
from .schemas import AddIncomeSchema, AddExpenseSchema, AddTransferSchema


async def add_transfer(
    id: str,
    query_bus: Annotated[QueryBus, Depends(lambda: di[QueryBus])],
    command_bus: Annotated[CommandBus, Depends(lambda: di[CommandBus])],
    access_token: Annotated[str, Depends(oauth2_scheme)],
    params: AddTransferSchema,
):
    """
    Add TransferMovement to user's account.
    """
    auth_token = cast(
        AuthTokenResponse,
        await query_bus.ask(FindAuthTokenQuery(access_token=access_token)),
    )
    command = AddTransferMovementCommand(
        **params.to_dict(), id=id, user_id=auth_token.user_id
    )
    await command_bus.dispatch(command)


async def add_income(
    id: str,
    query_bus: Annotated[QueryBus, Depends(lambda: di[QueryBus])],
    command_bus: Annotated[CommandBus, Depends(lambda: di[CommandBus])],
    access_token: Annotated[str, Depends(oauth2_scheme)],
    params: AddIncomeSchema,
):
    """
    Add IncomeMovement to user's account.
    """
    auth_token = cast(
        AuthTokenResponse,
        await query_bus.ask(FindAuthTokenQuery(access_token=access_token)),
    )
    command = AddIncomeMovementCommand(
        **params.to_dict(), id=id, user_id=auth_token.user_id
    )
    await command_bus.dispatch(command)


async def add_expense(
    id: str,
    query_bus: Annotated[QueryBus, Depends(lambda: di[QueryBus])],
    command_bus: Annotated[CommandBus, Depends(lambda: di[CommandBus])],
    access_token: Annotated[str, Depends(oauth2_scheme)],
    params: AddExpenseSchema,
):
    """
    Add ExpenseMovement to user's account.
    """
    auth_token = cast(
        AuthTokenResponse,
        await query_bus.ask(FindAuthTokenQuery(access_token=access_token)),
    )
    command = AddExpenseMovementCommand(
        **params.to_dict(), id=id, user_id=auth_token.user_id
    )
    await command_bus.dispatch(command)
