from pathlib import Path
from typing import AsyncGenerator

import pytest
from faker import Faker
from motor.core import AgnosticDatabase
from pyinstrument import Profiler

from src.planner.shared.infrastructure.persistence.motor.db import database
from src.shared.infrastructure.dependency_injector import init as init_dependencies
from tests.src.planner.shared.infrastructure.persistence.sqlalchemy.session import (
    SqlalchemyAutoRollbackSession,
)

init_dependencies()
TESTS_ROOT = Path.cwd()


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
def fake() -> Faker:
    return Faker()


@pytest.mark.asyncio
@pytest.fixture(scope="function")
async def sqlalchemy_sessionmaker() -> AsyncGenerator:
    sessionmaker = SqlalchemyAutoRollbackSession()
    await sessionmaker.begin()
    yield sessionmaker
    await sessionmaker.roolback()


@pytest.mark.asyncio
@pytest.fixture(scope="function")
def motor_database() -> AgnosticDatabase:
    return database("mercury_test")


@pytest.fixture(autouse=True)
def auto_profile(request):
    PROFILE_ROOT = TESTS_ROOT / ".profiles"
    profiler = Profiler()
    profiler.start()

    yield

    profiler.stop()
    PROFILE_ROOT.mkdir(exist_ok=True)

    try:
        name = request.node.cls.__name__
    except AttributeError:
        name = request.module.__name__

    results_file = PROFILE_ROOT / f"{name}#{request.node.name}.html"
    profiler.write_html(results_file)
