import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.8


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price(item2) == 100000


def test_apply_discount():
    assert Item.apply_discount(item1) == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_instantiate_from_csv_raise():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    assert Item.__repr__(item1) == "Item('Смартфон', 10000, 20)"
    assert Item.__repr__(item2) == "Item('Ноутбук', 20000, 5)"


def test_str():
    assert Item.__str__(item1) == 'Смартфон'
    assert Item.__str__(item2) == 'Ноутбук'


def test_phone_creation():
    phone = Phone("Phone Model", 1000, 10, 2)
    assert phone.name == "Phone Model"
    assert phone.price == 1000
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


def test_phone_addition_with_item():
    phone = Phone("Phone Model", 1000, 10, 2)
    item = Item("Item Model", 500, 5)
    result = item + phone
    assert result == 15


def test_phone_addition_with_phone():
    phone1 = Phone("Phone Model 1", 1000, 10, 2)
    phone2 = Phone("Phone Model 2", 1200, 8, 1)
    result = phone1 + phone2
    assert result == 18
