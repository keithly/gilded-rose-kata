from gilded_rose import Item, GildedRose
from constants import BRIE, SULFURAS, BACKSTAGE_PASS, CONJURED, NORMAL


def test_is_normal_or_conjured_brie():
    gilded_rose = GildedRose([])

    result = gilded_rose.is_normal_or_conjured(Item(BRIE, 1, 2))

    assert result is False


def test_is_normal_or_conjured_sulfuras():
    gilded_rose = GildedRose([])

    result = gilded_rose.is_normal_or_conjured(Item(SULFURAS, 1, 2))

    assert result is False


def test_is_normal_or_conjured_backstage_pass():
    gilded_rose = GildedRose([])

    result = gilded_rose.is_normal_or_conjured(Item(BACKSTAGE_PASS, 1, 2))

    assert result is False


def test_is_normal_or_conjured_normal():
    gilded_rose = GildedRose([])

    result = gilded_rose.is_normal_or_conjured(Item(NORMAL, 1, 2))

    assert result is True


def test_is_normal_or_conjured_conjured():
    gilded_rose = GildedRose([])

    result = gilded_rose.is_normal_or_conjured(Item(CONJURED, 1, 2))

    assert result is True
