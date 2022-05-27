from typing import Any, AsyncGenerator, Optional, List

import pytest
from httpx import AsyncClient
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, Session, SQLModel, Relationship

from sqladmin.forms import get_model_form
from tests.common import sync_engine as engine

pytestmark = pytest.mark.anyio

LocalSession = sessionmaker(bind=engine, class_=Session)

session: Session = LocalSession()


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=5)
    secret_name: str
    age: Optional[int] = None

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")


@pytest.fixture
def prepare_database() -> AsyncGenerator[None, None]:
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
async def client(prepare_database: Any) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url="http://testserver") as c:
        yield c


async def test_model_form_converter_exception(client: AsyncClient) -> None:
    await get_model_form(model=Hero, engine=engine)


def test_admin_supports_relationship() -> None:
    ...