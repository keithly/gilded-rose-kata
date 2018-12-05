from constants import BRIE, SULFURAS, BACKSTAGE_PASS, CONJURED


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == BRIE:
                if item.sell_in > 0:
                    item.quality = item.quality + 1
                else:
                    item.quality = item.quality + 2

            if item.name == BACKSTAGE_PASS:
                if item.sell_in > 10:
                    item.quality = item.quality + 1
                elif 11 > item.sell_in > 5:
                    item.quality = item.quality + 2
                elif 6 > item.sell_in > 0:
                    item.quality = item.quality + 3
                else:
                    item.quality = 0

            if item.name not in [SULFURAS, BRIE, BACKSTAGE_PASS] and item.quality > 0:
                if item.sell_in > 0:
                    if item.name.startswith(CONJURED):
                        item.quality = item.quality - 2
                    else:
                        item.quality = item.quality - 1
                else:
                    if item.name.startswith(CONJURED):
                        item.quality = item.quality - 4
                    else:
                        item.quality = item.quality - 2

            if item.quality > 50 and item.name != SULFURAS:
                item.quality = 50

            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
