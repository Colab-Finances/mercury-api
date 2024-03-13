from dataclasses import dataclass, field
from uuid import uuid4

from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.shared.domain.movements.events import IncomeMovementAdded
from tests.src.shared.domain.factories import AggregateRootFactory, EventDomainFactory

from .base import MovementAddedFactory, MovementFactory


@dataclass
class IncomeMovementFactory(AggregateRootFactory[IncomeMovement], MovementFactory):
    _AgregateClass = IncomeMovement

    account_id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class IncomeMovementAddedFactory(
    EventDomainFactory[IncomeMovementAdded], MovementAddedFactory
):
    _EventClass = IncomeMovementAdded

    account_id: str = field(default_factory=lambda: str(uuid4()))
