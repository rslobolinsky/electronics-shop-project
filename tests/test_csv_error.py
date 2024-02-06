import pytest

from src.InstantiateCSVError import InstantiateCSVError
from src.item import Item


def test_broken_csv():
    with pytest.raises(InstantiateCSVError):
        a = '../src/items.csv'
        Item.instantiate_from_csv(a)


def test_csv_notfound():
    with pytest.raises(FileNotFoundError):
        a = 'items.csv'
        Item.instantiate_from_csv(a)