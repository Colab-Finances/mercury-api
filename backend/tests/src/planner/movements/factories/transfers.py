from dataclasses import dataclass, field
from uuid import uuid4

from src.planner.movements.domain.transfers.aggregate import TransferMovement
from src.planner.shared.domain.movements.events import TransferMovementAdded
from tests.src.shared.domain.factories import AggregateRootFactory, EventDomainFactory

from .base import MovementAddedFactory, MovementFactory


@dataclass
class TransferMovementFactory(AggregateRootFactory[TransferMovement], MovementFactory):
    _AgregateClass = TransferMovement

    origin_id: str = field(default_factory=lambda: str(uuid4()))
    destination_id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class TransferMovementAddedFactory(
    EventDomainFactory[TransferMovementAdded], MovementAddedFactory
):
    _EventClass = TransferMovementAdded

    origin_id: str = field(default_factory=lambda: str(uuid4()))
    destination_id: str = field(default_factory=lambda: str(uuid4()))
