from typing import ClassVar, Dict, Generic, Protocol, Type, TypeVar, runtime_checkable

T_QueryResponse = TypeVar("T_QueryResponse", bound="QueryResponse")
T_Query = TypeVar("T_Query", bound="Query")


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


@runtime_checkable
class QueryHandler(Protocol, Generic[T_Query]):
    QUERY: Type[T_Query]

    async def __call__(self, query: Query[T_QueryResponse]) -> T_QueryResponse:
        ...
