from dataclasses import dataclass

from src.planner.shared.domain.bus.command import Command
from src.planner.users.domain.value_objects.pronoun import Pronoun


@dataclass(frozen=True)
class RegisterUserCommand(Command):
    id: str
    email: str
    name: str
    last_name: str
    password: str
    pronoun: Pronoun
