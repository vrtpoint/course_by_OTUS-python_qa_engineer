import pytest


@pytest.fixture(scope="function")
def creation_list():
    items_list = [1, 21, 2, 5,'тест', 'pytest']
    return items_list

@pytest.fixture(scope="function")
def list_of_data():
    items_list = ["pytest", 5, 'i', ("один", 1), 6]
    return items_list

@pytest.fixture(autouse=True)
def remove_element():
    items_list = [1,2,5,'тест']
    items_list.remove('тест')
    print(items_list)
    return items_list

@pytest.fixture()
def create_list():
    items_list = list(range(5))
    return items_list