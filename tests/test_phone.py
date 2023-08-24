import pytest
from src.item import Item, TempClass
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("Oppo", 39990, 20, 20)


@pytest.fixture
def item():
    return Item("iPhone 14", 120_000, 5)


@pytest.fixture
def t_class():
    return TempClass(10)


def test_str(phone):
    assert phone.__str__() == "Oppo"


def test_add(item, phone, t_class):
    assert item + phone == 25
    with pytest.raises(ValueError):
        phone + t_class.quantity
    with pytest.raises(ValueError):
        item + t_class



