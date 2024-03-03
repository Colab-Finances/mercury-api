from fastapi import APIRouter, status

from .controllers import add_income, add_expense, add_transfer

router = APIRouter()

router.add_api_route(
    "/v1/movements/incomes/{id}",
    methods=["POST"],
    endpoint=add_income,
    tags=["incomes"],
    status_code=status.HTTP_201_CREATED,
)

router.add_api_route(
    "/v1/movements/expenses/{id}",
    methods=["POST"],
    endpoint=add_expense,
    tags=["expenses"],
    status_code=status.HTTP_201_CREATED,
)

router.add_api_route(
    "/v1/movements/transfers/{id}",
    methods=["POST"],
    endpoint=add_transfer,
    tags=["transfers"],
    status_code=status.HTTP_201_CREATED,
)
