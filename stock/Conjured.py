from NormalItem import NormalItem
from tests import manaCake

class Conjured(NormalItem):

    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

