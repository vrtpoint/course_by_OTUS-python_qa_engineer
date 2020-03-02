import pytest


@pytest.fixture(scope="function")
def creation_dictionary():
    items_dictionary = {1: "Tom", "2": True, 3: 100.6}
    return items_dictionary