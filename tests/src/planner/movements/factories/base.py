from dataclasses import dataclass, field
from uuid import uuid4

from faker import Faker

from src.planner.shared.domain.value_objects.date import DATE_FORMAT

fake = Faker()


@dataclass
class MovementFactory:
    id: str = field(default_factory=lambda: str(uuid4()))
    account_owner_id: str = field(default_factory=lambda: str(uuid4()))
    amount: int = field(default_factory=fake.pyint)
    date: str = field(default_factory=lambda: fake.date_object().strftime(DATE_FORMAT))


@dataclass
class MovementAddedFactory:
    amount: int = field(default_factory=fake.pyint)
    date: str = field(default_factory=lambda: fake.date_object().strftime(DATE_FORMAT))
