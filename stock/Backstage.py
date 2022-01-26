from tkinter import N
from NormalItem import NormalItem
from tests import backstage1 , backstage2 , backstage3

class Backstage(NormalItem):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)