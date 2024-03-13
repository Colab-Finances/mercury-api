from dataclasses import dataclass, field
from uuid import uuid4

from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.shared.domain.movements.events import ExpenseMovementAdded
from tests.src.shared.domain.factories import AggregateRootFactory, EventDomainFactory

from .base import MovementAddedFactory, MovementFactory


@dataclass
class ExpenseMovementFactory(AggregateRootFactory[ExpenseMovement], MovementFactory):
    _AgregateClass = ExpenseMovement

    account_id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class ExpenseMovementAddedFactory(
    EventDomainFactory[ExpenseMovementAdded], MovementAddedFactory
):
    _EventClass = ExpenseMovementAdded

    account_id: str = field(default_factory=lambda: str(uuid4()))
