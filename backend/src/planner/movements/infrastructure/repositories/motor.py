from typing import List, Optional

from kink import inject

from src.planner.movements.domain.aggregate import Movement
from src.planner.movements.domain.expenses.aggregate import ExpenseMovement
from src.planner.movements.domain.incomes.aggregate import IncomeMovement
from src.planner.movements.domain.repository import MovementRepository, MovementType
from src.planner.movements.domain.transfers.aggregate import TransferMovement
from src.planner.movements.domain.value_objects.id import MovementId
from src.planner.shared.application.mappers import dict_to_entity
from src.planner.shared.domain.users.id import UserId
from src.planner.shared.infrastructure.persistence.motor.repositories import (
    MotorRepository,
)


@inject(alias=MovementRepository, use_factory=True)
class MotorMovementRepository(MotorRepository):
    COLLECTION_NAME = "planner__movements"
    TYPES = {
        "ExpenseMovement": ExpenseMovement,
        "IncomeMovement": IncomeMovement,
        "TransferMovement": TransferMovement,
    }

    async def save(self, movement: Movement) -> None:
        await self.collection.update_one(
            {"id": movement.id.value},
            {"$set": self._aggregate_to_dict(movement)},
            upsert=True,
        )

    async def search(self, id: MovementId) -> Optional[MovementType]:
        """Search object by id"""
        result = await self.collection.find_one({"id": id.value})
        if not result:
            return None

        return dict_to_entity(result, self.TYPES[result["_type"]])  # type: ignore[arg-type]

    async def match(self, account_owner_id: UserId) -> List[MovementType]:
        """Match all movements by account owner id"""
        cursor = self.collection.find({"account_owner_id": account_owner_id.value})
        result = await cursor.to_list(None)
        return [dict_to_entity(data, self.TYPES[data["_type"]]) for data in result]  # type: ignore[arg-type]  # noqa: E501

    def _aggregate_to_dict(self, aggregate) -> dict:
        data = super()._aggregate_to_dict(aggregate)
        data["_type"] = type(aggregate).__name__
        return data
