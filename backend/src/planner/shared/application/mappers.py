from typing import Any, Dict, TypeVar

from src.planner.shared.domain.aggregates import AggregateRoot
from src.planner.shared.domain.bus.query import QueryResponse

Aggregate = TypeVar("Aggregate", bound=AggregateRoot)


def dict_to_entity(data: Dict[str, Any], entity_class: type[Aggregate]) -> Aggregate:
    """Create a Entity from a dict.
    Used for deserialization of a AggregateRoot. Usually used in a Database.

    Args:
        data (dict[str, Any]): A dict with the attributes of a Entity
        entity_class (AggregateRoot): A Entity class(like User, AuthCredential, etc)

    Returns:
        Entity
    """
    annotations = entity_class.__init__.__annotations__
    attributes = {
        key: annotations[key](value)
        for key, value in data.items()
        if key in annotations
    }
    return entity_class(**attributes)


QR = TypeVar("QR", bound=QueryResponse)


def entity_to_response(entity: AggregateRoot, response: type[QR]) -> QR:
    annotations = filter(
        lambda key: key != "return", response.__init__.__annotations__.keys()
    )
    attributes = {key: getattr(entity, key).primitive for key in annotations}
    return response(**attributes)
