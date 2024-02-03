from dataclasses import dataclass, field
from uuid import uuid4

from faker import Faker

from src.planner.expenses.domain.entity import Expense
from src.planner.shared.domain.value_objects.date import DATE_FORMAT
from tests.src.shared.domain.factories import AggregateRootFactory

fake = Faker()


@dataclass
class ExpenseFactory(AggregateRootFactory[Expense]):
    _AgregateClass = Expense

    id: str = field(default_factory=lambda: str(uuid4()))
    amount: int = field(default_factory=fake.pyint)
    account_id: str = field(default_factory=lambda: str(uuid4()))
    date: str = field(default_factory=lambda: fake.date_object().strftime(DATE_FORMAT))
