from typing import ClassVar, Dict, Generic, Protocol, Type, TypeVar, runtime_checkable

T_QueryResponse = TypeVar("T_QueryResponse", bound="QueryResponse")


@runtime_checkable
class QueryResponse(Protocol):
    __dataclass_fields__: ClassVar[Dict]


@runtime_checkable
class Query(Protocol, Generic[T_QueryResponse]):
    RESPONSE: Type[T_QueryResponse]
    __dataclass_fields__: ClassVar[Dict]


@runtime_checkable
class QueryBus(Protocol):
    async def ask(self, query: Query[T_QueryResponse]) -> T_QueryResponse:
        ...
