from typing import cast

from kink import inject

from src.planner.shared.domain.users import UserId
from src.planner.users.domain.value_objects import UserAvatar

from .avatar_updater import UserAvatarUpdater
from .command import UpdateUserAvatarCommand


@inject
class UpdateUserAvatarCommandHandler:
    def __init__(self, use_case: UserAvatarUpdater) -> None:
        self.use_case = use_case

    async def __call__(self, command: UpdateUserAvatarCommand) -> None:
        avatar = UserAvatar.make(command.avatar)  # type: ignore[arg-type]
        avatar = cast(UserAvatar, avatar)
        await self.use_case(
            id=UserId(command.id),
            avatar=avatar,
            current_user_id=UserId(command.user_id),
        )
