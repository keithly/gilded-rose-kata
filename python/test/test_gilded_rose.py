from gilded_rose import Item, GildedRose
from constants import NORMAL, BRIE


def test_update_quality_name_is_found():
    items = [Item(NORMAL, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].name == NORMAL


def test_iteration_occurs():
    items = [Item(NORMAL, 1, 2),
             Item(BRIE, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].name == NORMAL
    assert items[0].sell_in == 0
    assert items[0].quality == 1

    assert items[1].name == BRIE
    assert items[1].sell_in == 0
    assert items[1].quality == 3
