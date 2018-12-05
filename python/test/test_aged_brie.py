from gilded_rose import Item, GildedRose
from constants import BRIE


def test_update_quality_brie_sell_in_decrements():
    items = [Item(BRIE, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 0


def test_update_quality_brie_quality_increments():
    items = [Item(BRIE, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 3


def test_update_quality_brie_past_sell_in_quality_improves_2x():
    # requirements don't specify that Aged Brie quality improves 2x past sell-in date
    # but that's what happens

    items = [Item(BRIE, 0, 4)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 6


def test_update_quality_brie_quality_does_not_exceed_50():
    items = [Item(BRIE, 1, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality <= 50
