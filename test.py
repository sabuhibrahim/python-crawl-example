import unittest
from data import SHOPS
from main import find_price

class CheckPriceList(unittest.TestCase):
    def test_return_value(self):
        for shop in SHOPS:
            prices = find_price(
                shop['url'],
                keyword=shop['keyword'],
                element=shop['element'],
                attr=shop['attr']
            )
            self.assertIn(type(prices), [type(None), type([])])



if __name__ == '__main__':
    unittest.main()