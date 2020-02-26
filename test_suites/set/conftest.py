import pytest


@pytest.fixture(autouse=True)
def create_set():
    users = set(["Mike", "Bill", "Ted"])
    return users

@pytest.fixture(autouse=True)
def create_frozen_set():
    users = frozenset({"Mike", "Bill", "Ted"})
    return users

@pytest.fixture
def add_unique_value():
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {2, 3, 4, 5, 6}
    set_1.update(set_2)
    return set_1