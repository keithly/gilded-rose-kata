from gilded_rose import Item, GildedRose
from constants import NORMAL


def test_update_quality_normal_item_sell_in_decrements():
    items = [Item(NORMAL, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 0


def test_update_quality_normal_item_quality_decrements():
    items = [Item(NORMAL, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 1


def test_update_quality_normal_item_past_sell_in_quality_degrades_2x():
    items = [Item(NORMAL, 0, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 0


def test_update_quality_normal_item_quality_not_negative():
    items = [Item(NORMAL, 1, 0)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 0


def test_update_quality_normal_item_quality_does_not_exceed_50():
    items = [Item(NORMAL, 1, 51)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 50
