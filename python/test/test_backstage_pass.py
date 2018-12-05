from gilded_rose import Item, GildedRose
from constants import BACKSTAGE_PASS


def test_update_quality_backstage_sell_in_decrements():
    items = [Item(BACKSTAGE_PASS, 1, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 0


def test_update_quality_backstage_quality_increments_sell_in_over_10():
    items = [Item(BACKSTAGE_PASS, 11, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 3


def test_update_quality_backstage_quality_inc_2_sell_in_within_10():
    items = [Item(BACKSTAGE_PASS, 10, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 4


def test_update_quality_backstage_quality_inc_3_sell_in_within_5():
    items = [Item(BACKSTAGE_PASS, 5, 2)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 5


def test_update_quality_backstage_quality_0_after_concert():
    items = [Item(BACKSTAGE_PASS, 0, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 0


def test_update_quality_backstage_quality_does_not_exceed_50():
    items = [Item(BACKSTAGE_PASS, 1, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 50
