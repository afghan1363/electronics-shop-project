import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def item():
    return Item("Смартфон", 60000, 10)


def test_item_calculate_total_price(item):
    assert item.calculate_total_price() == 600000


def test_item_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.pay_rate * 60000 == item.price


def test_name(item):
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_repr(item):
    assert item.__repr__() == "Item(Смартфон, 60000, 10)"

def test_str(item):
    item.name = "СуперСмартфон"
    assert  item.__str__() == "СуперСмарт"
