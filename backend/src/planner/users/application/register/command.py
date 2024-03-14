from dataclasses import dataclass

from src.planner.users.domain.value_objects.pronoun import Pronoun
from src.planner.shared.domain.bus.command import Command


@dataclass(frozen=True)
class RegisterUserCommand(Command):
    id: str
    email: str
    name: str
    last_name: str
    password: str
    pronoun: Pronoun
