"""User respository"""
from typing import Optional

from kink import inject
from sqlalchemy import UUID, Boolean, Column, DateTime, Enum, String, select

from src.planner.shared.infrastructure.persistence.sqlalchemy.models import Base
from src.planner.shared.infrastructure.persistence.sqlalchemy.repositories import (
    SqlAlchemyCreateMixin,
    SqlAlchemyFindMixin,
    SqlAlchemyRepository,
    SqlAlchemySaveMixin,
)
from src.planner.users.domain.entity import User
from src.planner.users.domain.repository import UserRepository
from src.planner.users.domain.value_objects import UserEmail, pronoun


class SqlAlchemyUser(Base):
    id = Column(UUID, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    email = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    pronoun = Column(  # type: ignore[var-annotated]
        Enum(
            pronoun.Pronoun,
            values_callable=lambda _: pronoun.Pronoun.keys(),
            name="pronouns",
        )
    )

    __tablename__ = "planner__users"


@inject(alias=UserRepository, use_factory=True)
class SqlAlchemyUserRepository(
    SqlAlchemyRepository,
    SqlAlchemyCreateMixin,
    SqlAlchemyFindMixin,
    SqlAlchemySaveMixin,
):
    model_class = SqlAlchemyUser
    entity_class = User

    async def search_by_email(self, email: UserEmail) -> Optional[User]:
        """Search user by email"""
        stmt = (
            select(SqlAlchemyUser).where(SqlAlchemyUser.email == email.value).limit(1)
        )
        return await self._search(stmt)
