import pytest
import responses


@pytest.fixture(autouse=True)
def reset_responses():
    responses.reset()
