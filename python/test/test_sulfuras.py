from gilded_rose import Item, GildedRose
from constants import SULFURAS


def test_update_quality_sulfuras_sell_in_no_change():
    items = [Item(SULFURAS, 1, 80)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 1


def test_update_quality_sulfuras_quality_stays_80():
    items = [Item(SULFURAS, 1, 80)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 80
