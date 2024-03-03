from fastapi import APIRouter, status

from src.planner.movements.application.responses import MovementResponse

from .controllers import add_expense, add_income, add_transfer, find

router = APIRouter()

router.add_api_route(
    "/v1/movements/{id}",
    methods=["GET"],
    endpoint=find,
    tags=["movements"],
    response_model=MovementResponse,
    status_code=status.HTTP_200_OK,
)

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
