import csv


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = f'Файл поврежден'


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
    def instantiate_from_csv(cls, file_name="../src/items.csv"):
        try:
            with open(file_name, newline="", encoding="utf-8") as csfile:
                reader = csv.DictReader(csfile)
                for row in reader:
                    try:
                        list_item = cls(row["name"], row["price"], row["quantity"])
                        if row["quantity"] == "" or row["price"] == "" or row["name"] == "":
                            raise InstantiateCSVError
                    except InstantiateCSVError as ex:
                        print(ex.message)
                    cls.all.append(list_item)

        except FileNotFoundError:
            print(f"Отсутствует файл {file_name}")

    @staticmethod
    def string_to_number(str_number):
        int_number = int(float(str_number))
        return int_number

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Ошибка")
