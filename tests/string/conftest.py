import pytest


@pytest.fixture(scope="function")
def сreate_phrase(request):
    print(f"\n from {request.scope} fixture!")
    phrase = "Pytest - тестовый фреймворк"
    return phrase

@pytest.fixture(scope="module")
def сoncatenate_phrase(request):
    print(f"\n from {request.scope} fixture!")
    part_1 = "Pytest -"
    part_2 = "тестовый фреймворк"
    phrase = part_1 + " " + part_2
    return phrase
