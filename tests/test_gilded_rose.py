# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_sell_date_passed(self):
        quality = 20
        sell_in = 0
        items = [Item("other_than_aged_brie", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality - 2, items[0].quality)

    def test_sell_date_passed_brie(self):
        quality = 10
        sell_in = -2
        items = [Item("Aged Brie", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 2, items[0].quality)

    def test_quality_drops_0_after_concert_date(self):
        quality = 40
        sell_in = -1
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sell_date_expire_sulfuras(self):
        quality = 40
        sell_in = 5
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in, items[0].sell_in)
        self.assertEqual(quality, items[0].quality)

    # def test_concert_quality_less_then_10_5_days(self):
    #     quality = 20
    #     sell_in = 12
    #     items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     if sell_in <= 10 and sell_in > 5:
    #         self.assertEqual(quality + 2, items[0].quality)
    #     elif sell_in <= 5 and sell_in >= 0:
    #         self.assertEqual(quality + 3, items[0].quality)
    #     else:
    #         self.assertEqual(quality + 1, items[0].quality)

    def test_normal_item_quality_zero_no_change(self):
        quality = 0
        sell_in  = 10
        items = [Item("foo", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality, items[0].quality)

    def test_aged_brie_quality_does_not_exceed_50(self):
        quality = 50
        sell_in  = 5
        items = [Item("Aged Brie", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality, items[0].quality)

    def test_backstage_pass_quality_does_not_exceed_50(self):
        quality = 50
        sell_in  = 8
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality, items[0].quality)

    def test_backstage_pass_quality_increase_by_2_when_10_days_or_less(self):
        quality = 20
        sell_in = 10
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 2, items[0].quality)

    def test_backstage_pass_quality_increase_by_3_when_5_days_or_less(self):
        quality = 20
        sell_in = 5
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 3, items[0].quality)

    def test_normal_item_expired_quality_zero_stays_zero(self):
        items = [Item("foo", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


# if __name__ == '__main__':
#     unittest.main()
