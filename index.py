from data import SHOPS
from main import find_price

# Find prices for every shop
for shop in SHOPS:
    prices = find_price(
        shop['url'],
        keyword=shop['keyword'],
        element=shop['element'],
        attr=shop['attr']
    )
    print(f"{shop['name']} | {str(prices or 'Product not found')}")
