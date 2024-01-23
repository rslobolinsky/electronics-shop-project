import pathlib

from src.item import Item


def test_check_len_item_all_if_len_zero():
    assert len(Item.all) == 0


def test_check_len_item_all_if_len_one(fixture_class_item):
    assert len(Item.all) == 1


def test_init_object_item(fixture_class_item):
    assert fixture_class_item.name == "Смартфон"
    assert fixture_class_item.price == 10000
    assert fixture_class_item.quantity == 20


def test_sum_total_price(fixture_class_item, fixture_class_item_2):
    assert fixture_class_item.calculate_total_price() == 10000 * 20
    assert fixture_class_item_2.calculate_total_price() == 100 * 666


def test_pay_rate(fixture_class_item, fixture_class_item_2):
    fixture_class_item.pay_rate = 0.5
    fixture_class_item.apply_discount()

    assert fixture_class_item.price == 10000 * 0.5
    assert fixture_class_item_2.price == 100
    assert fixture_class_item.calculate_total_price() == (10000 * 0.5) * 20
    assert fixture_class_item.pay_rate == 0.5


def test_item_all(fixture_class_item, fixture_class_item_2):
    for value in Item.all:
        assert isinstance(value, object)


def test_getter_and_setter(fixture_class_item):
    item = fixture_class_item
    item.name = "smartphoneOne"
    assert item.name == "smartphone"

    item.name = "smart"
    assert item.name == "Smart"

    item.name = 111
    assert item.name == "111"


def test_instantiate_from_csv():
    ROOT = pathlib.Path(__file__).parent.parent
    Item.instantiate_from_csv(pathlib.Path.joinpath(ROOT / 'src/items.csv'))

    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('2.5') == 2
    assert Item.string_to_number('2,5') == 2

def test_metods_repr_and_str():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"
    assert str(item) == 'Смартфон'

