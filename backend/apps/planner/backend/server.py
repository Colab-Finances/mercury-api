from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

from apps.planner.backend.config import settings
from apps.planner.backend.shared.urls import router
from src.planner.shared.domain.exceptions.base import DomainException
from src.shared.infrastructure.dependency_injector import init as init_dependencies

init_dependencies()

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_PREFIX}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)[:-1] for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if settings.PROFILING and settings.ENVIROMENT != "production":
    from pyinstrument import Profiler

    @app.middleware("http")
    async def profile_request(request: Request, call_next):
        profiling = request.query_params.get("profile", False)
        if profiling:
            profiler = Profiler(async_mode="enabled")
            profiler.start()
            await call_next(request)
            profiler.stop()
            return HTMLResponse(profiler.output_html())
        else:
            return await call_next(request)


app.include_router(router, prefix=settings.API_PREFIX)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    data = ({"source": err["loc"][1], "msg": err["msg"]} for err in exc.errors())
    return JSONResponse({"detail": tuple(data)}, status_code=422)


@app.exception_handler(DomainException)
async def base_error_handler(request, exception):
    return JSONResponse({"detail": [dict(exception)]}, status_code=exception.code)
