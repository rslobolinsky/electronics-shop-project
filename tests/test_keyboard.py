import pytest

from src.item import Item
from src.keyboard import Keyboard, Mixin

@pytest.fixture
def fixture_class():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_class(fixture_class):
    assert isinstance(fixture_class, object)
    assert issubclass(Keyboard, Item)
    assert issubclass(Keyboard, Mixin)
    assert str(fixture_class) == "Dark Project KD87A"

def test_lang_in_kb(fixture_class):
    assert fixture_class.language == 'EN'

    fixture_class.change_lang()
    assert fixture_class.language == 'RU'

    fixture_class.change_lang()
    assert fixture_class.language == 'EN'