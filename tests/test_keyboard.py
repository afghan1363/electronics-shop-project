import pytest
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def k_board():
    return Keyboard('UltraSuperKlava', 30000, 50)


def test_keyboard_name(k_board):
    assert k_board.name == "UltraSuperKlava"


def test_keyboard_language(k_board):
    assert k_board.language == "EN"
    with pytest.raises(AttributeError):
        k_board.language = 'CH'


def test_change_lang(k_board):
    k_board.change_lang()
    assert str(k_board.language) == "RU"
    k_board.change_lang()
    assert str(k_board.language) == "EN"
    k_board.change_lang().change_lang()
    assert str(k_board.language) == "EN"
