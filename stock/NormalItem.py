from Item import Item
from tests import dexVest

class NormalItem(Item):

    def __init__(self, name, sellIn, quality):
        super().__init__(self, name, sellIn, quality)
    
    def reduceSellIn(self  ):
        self.sell_in -= 1

    def changeQuality(self):
        qualityModifier = -1
        if self.sell_in < 0:
            qualityModifier *= 2
        self.quality += qualityModifier
    
    def checkQuality(self):
        if self.quality <= 0: self.quality = 0
        if self.quality >= 50: self.quality = 50
    
    def updateQuality(self):
        self.reduceSellIn()
        self.changeQuality()
        self.checkQualityInRange()
    
