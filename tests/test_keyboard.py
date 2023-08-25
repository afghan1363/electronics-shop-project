import pytest
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def k_board():
    return Keyboard('UltraSuperKlava', 30000, 50)

@pytest.fixture
def item():
    return Item("Смартфон", 60000, 10)


def test_keyboard_language(k_board):
    assert k_board.language == "EN"


def test_change_lang(k_board):
    k_board.change_lang()
    assert str(k_board.language) == "RU"

