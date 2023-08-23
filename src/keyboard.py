from src.item import Item


class MixinLang:
    language = 'EN'

    def change_lang(self):
        if self.language.strip().upper() == 'RU':
            self.language = 'EN'
        elif self.language.strip().upper() == 'EN':
            self.language = 'RU'
        return self


class Keyboard(MixinLang, Item):

    def __init__(self, name: str, price: float, quantity=1):
        super().__init__(name, price, quantity)

    def __str__(self):
        return f'{self.name}'
