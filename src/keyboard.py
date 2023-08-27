from src.item import Item


class Mixin:
    """Класс для реализации выбора раскладки для товара 'клавиатура'"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Mixin, Item):
    """Класс товара 'клавиатура' с выбором раскладки"""
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
