from typing import Union

from src.planner.movements.domain.aggregate import Movement
from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.movements.domain.transfers.aggregate import TransferMovement

from .responses import (
    ExpenseMovementResponse,
    IncomeMovementResponse,
    MovementResponse,
    TransferMovementResponse,
)

responses = {
    ExpenseMovement: ExpenseMovementResponse,
    IncomeMovement: IncomeMovementResponse,
    TransferMovement: TransferMovementResponse,
}


def entity_to_response(
    entity: Union[ExpenseMovement, IncomeMovement, TransferMovement]
) -> MovementResponse:
    if not isinstance(entity, Movement):
        raise RuntimeError(f"Entity {entity} is not a valid Movement")

    # TODO: Cast to SingleResponse type
    return responses[type(entity)].from_entity(entity)  # type: ignore[attr-defined]
