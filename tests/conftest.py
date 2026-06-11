import copy

import pytest

from src import app


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the app's in-memory activities after each test."""
    original = copy.deepcopy(app.activities)
    yield
    app.activities = original
