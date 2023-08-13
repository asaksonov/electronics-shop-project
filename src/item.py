import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
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

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.__name}\', {round(self.price)}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[0:10]
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        discount_price = self.price * self.pay_rate
        self.price = discount_price
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open("../src/items.csv", newline="", encoding="utf-8") as csfile:
            reader = csv.DictReader(csfile)
            for row in reader:
                print(row["name"], row["price"], row["quantity"])
                list_item = cls(row["name"], row["price"], row["quantity"])
                cls.all.append(list_item)

    @staticmethod
    def string_to_number(str_number):
        int_number = int(float(str_number))
        return int_number
