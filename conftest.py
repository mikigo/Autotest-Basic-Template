import pytest

# fixtures


@pytest.fixture(scope="session")
def check():
    from method.asserts import Asserts
    return Asserts