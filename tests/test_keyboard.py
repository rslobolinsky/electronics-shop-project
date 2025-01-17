import pytest

from src.item import Item
from src.keyboard import Keyboard, Mixin


@pytest.fixture
def fixture_class():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_class(fixture_class):
    assert isinstance(fixture_class, object)
    assert issubclass(Keyboard, Item)
    assert issubclass(Keyboard, Mixin)
    assert str(fixture_class) == "Dark Proje"


def test_lang_in_kb(fixture_class):
    assert fixture_class.language == 'EN'

    fixture_class.change_lang()
    assert fixture_class.language == 'EN'

    fixture_class.change_lang()
    assert fixture_class.language == 'EN'


# def __add__(self, other):
#     if isinstance(other, Item):
#         return self.quantity + other.quantity
#     raise ValueError
