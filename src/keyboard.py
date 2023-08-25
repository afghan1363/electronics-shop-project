from src.item import Item


class Mixin:
    language = "EN"
    
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = Mixin.language
        Mixin.language = self.language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self


class Keyboard(Mixin, Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
# self.language = "EN"
