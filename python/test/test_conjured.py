from gilded_rose import Item, GildedRose
from constants import CONJURED


def test_update_quality_conjured_item_sell_in_decrements():
    items = [Item(CONJURED, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 0


def test_update_quality_conjured_item_quality_degrades_2x():
    items = [Item(CONJURED, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 0


def test_update_quality_conjured_item_past_sell_in_quality_degrades_4x():
    items = [Item(CONJURED, 0, 4)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 0


def test_update_quality_conjured_item_quality_not_negative():
    items = [Item(CONJURED, 1, 0)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 0


def test_update_quality_conjured_item_quality_does_not_exceed_50():
    items = [Item(CONJURED, 1, 51)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality <= 50
