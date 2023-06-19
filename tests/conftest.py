import os
import pytest
from glob import glob
from feathr_bot.app import create_app


pytest_plugins = [
    fixture_file.replace("/", ".").replace(".py", "")
    for fixture_file in glob("tests/fixtures/[!__]*.py", recursive=True)
]


@pytest.fixture()
def app():
    app = create_app("testing")

    yield app


@pytest.fixture()
def client():
    app = create_app("testing")

    client = app.test_client()

    yield client
