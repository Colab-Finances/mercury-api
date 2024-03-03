from dataclasses import dataclass

from src.planner.users.application.find.responses import UserResponse


@dataclass(frozen=True)
class FindUserQuery:
    RESPONSE = UserResponse
    id: str
    user_id: str
