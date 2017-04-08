# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption("--path", action="store", default="/opt",
                     help="Path: path of the directory")


@pytest.fixture
def path(request):
    return request.config.getoption("--path")
