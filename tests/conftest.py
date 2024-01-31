import pytest

from src.item import Item


@pytest.fixture
def fixture_class_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def fixture_class_item_2():
    return Item("No Смартфон", 100, 666)
    item.name = "111"
    assert item.name == "111"
    assert phone + item == 25
    with pytest.raises(ValueError):
        phone + 5