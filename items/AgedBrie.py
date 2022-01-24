from NormalItem import NormalItem
from tests import agedBrie


class AgedBrie(NormalItem):

    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def changeQuality(self):
        qualityModifier = 1
        if self.sell_in < 0:
            qualityModifier *= 2
        self.quality += qualityModifier

