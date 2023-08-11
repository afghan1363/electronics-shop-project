import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""
@pytest.fixture
def item():
    return Item("Notebook", 60000, 10)

def test_item_calculate_total_price(item):
    assert item.calculate_total_price() == 600000

def test_item_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.pay_rate * 60000 == item.price
