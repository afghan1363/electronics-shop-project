import csv
import os.path
from abc import ABC, abstractmethod
from os import path

from src.exceptions import InstantiateCSVError


class Item(ABC):
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

    def __add__(self, other):
        """Сложение атрибутов класса и его подклассов"""
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError("Сложение атрибутов неродственных классов")

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

    """
    Я сделал два варианта работы. В одном исключения обрабатываются try - except,
    в другом исключения выбрасываются с сообщением. У нас со студентами спор возник, как надо, вот и сделал
    оба варианта, на всякий случай
    """
    # @classmethod
    # def instantiate_from_csv(cls):                            # Первый вариант
    #     """Создание экземпляров класса из файла .csv"""
    #     path_to_csv = os.path.join("..", "src", "items_damaged.csv")
    #     file_name = os.path.basename(path_to_csv)
    #     try:
    #         with open(path_to_csv, encoding="cp1251") as csv_data:
    #             reader = csv.DictReader(csv_data, delimiter=",")
    #             row_keys = ("name", "price", "quantity")
    #             for row in reader:
    #                 if row_keys[0] and row_keys[1] and row_keys[2] in row:
    #                     item = cls(row["name"], row["price"], row["quantity"])
    #                 else:
    #                     raise InstantiateCSVError(file_name)
    #     except FileNotFoundError:
    #         print(f"Отсутствует файл {file_name}")
    #     except InstantiateCSVError as ex:
    #         print(ex.__str__())

    @classmethod
    def instantiate_from_csv(cls, path_to_csv=None):                                      # Второй вариант
        """
        Создание экземпляров класса из файла csv
        """
        path_to_csv = os.path.join("..", "src", "items_damaged.csv")
        file_name = os.path.basename(path_to_csv)
        if not path.exists(path_to_csv):
            raise FileNotFoundError(f"Файл {file_name} не найден")
        else:
            with open(path_to_csv, encoding="cp1251") as csv_data:
                reader = csv.DictReader(csv_data, delimiter=",")
                row_keys = ("name", "price", "quantity")
                for row in reader:
                    if row_keys[0] and row_keys[1] and row_keys[2] in row:
                        item = cls(row["name"], row["price"], row["quantity"])
                    else:
                        raise InstantiateCSVError(file_name)



    @staticmethod
    def string_to_number(str_int):
        return int(float(str_int))


class TempClass:
    """Класс для теста"""

    def __init__(self, quantity):
        self.quantity = quantity


if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    print(Item.instantiate_from_csv())
