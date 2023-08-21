from src.item import Item


class MixinLang:
    LANG = 'EN'

    def __init__(self, name, price, quantity):
        self.__language = self.LANG
        super().__init__(name, price, quantity)

    def change_lang(self):
        if self.__language.strip().upper() == 'RU':
            self.language = 'EN'
        elif self.__language.strip().upper() == 'EN':
            self.language = 'RU'
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_lng: str):
        if new_lng.strip().upper() not in ('RU', 'EN'):
            raise ValueError('язык клавиатуры должен быть или RU или EN')
        self.__language = new_lng.strip().upper()


class Keyboard(MixinLang, Item):

    def __init__(self, name: str, price: float, quantity=1):
        super().__init__(name, price, quantity)

    def __str__(self):
        return f'{self.name}'
