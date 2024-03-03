from datetime import date, datetime

from src.planner.shared.domain.value_objects.base import ValueObject

DATE_FORMAT = "%d-%m-%Y"


class DateValueObject(ValueObject[date]):
    BASE_TYPE = date

    def _cast(self, value: str) -> date:
        if value is None:
            self._fail("Is required")
        if isinstance(value, datetime):  # Date is a subclass of datetime
            return value.date()
        if isinstance(value, date):
            return value
        try:
            return datetime.strptime(value, DATE_FORMAT).date()
        except Exception:
            self._fail(f"Invalid {self.BASE_TYPE.__name__}")
            return None  # type: ignore[return-value]

    @property
    def primitive(self) -> str:  # type: ignore[override]
        """
        Transform date value to string
        """
        return self.value.strftime(DATE_FORMAT)
