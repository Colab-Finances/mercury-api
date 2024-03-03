from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from apps.planner.backend.server import app


@pytest.fixture(scope="module")
async def client() -> AsyncGenerator:
    transport = ASGITransport(app=app)  # type: ignore[arg-type]
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        yield ac
