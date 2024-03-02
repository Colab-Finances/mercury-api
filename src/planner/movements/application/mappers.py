from src.planner.movements.domain.aggregate import Movement
from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.movements.domain.transfers.aggregate import TransferMovement
from src.planner.shared.application.mappers import (
    entity_to_response as shared_entity_to_response,
)

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


def entity_to_response(entity: Movement) -> MovementResponse:
    if not isinstance(entity, Movement):
        raise RuntimeError(f"Entity {entity} is not a valid Movement")

    response_class = responses[type(entity)]
    return shared_entity_to_response(entity, response_class)
