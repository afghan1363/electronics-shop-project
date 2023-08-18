import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        if len(name_str) > 10:
            self.__name = name_str[:10]
        else:
            self.__name = name_str

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        """
        Информация о классе: значения экземпляров.
        """
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Информация о классе: значение поля self.name
        """
        return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        path_to_csv = os.path.join("..", "src", "items.csv")
        with open(path_to_csv, encoding="cp1251") as csv_data:
            reader = csv.DictReader(csv_data, delimiter=",")
            for row in reader:
                item = cls(row["name"], row["price"], row["quantity"])

    @staticmethod
    def string_to_number(str_int):
        return int(float(str_int))
