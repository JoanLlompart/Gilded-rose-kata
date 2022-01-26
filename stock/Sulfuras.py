from NormalItem import NormalItem
from tests import sulfuras1, sulfuras2

class Sulfuras(NormalItem):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality