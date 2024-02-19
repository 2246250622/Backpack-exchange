"""
注册链接：https://backpack.exchange/refer/51bitquant
"""

import time
from api import BackpackClient
from config import *
from decimal import Decimal, ROUND_DOWN
from typing import Union


def floor_to(value: Union[Decimal, float, int], target: Union[Decimal, float, int]) -> Decimal:
    """
    Similar to math.floor function, but to target float number.
    """
    value = Decimal(str(value))
    target = Decimal(str(target).rstrip("0"))
    result = value.quantize(target, rounding=ROUND_DOWN)

    return result


if __name__ == '__main__':
    client = BackpackClient(api_key=api_key, api_secret=api_secret)
    trade_pair.replace("/", "_")
    precision = Decimal("1")/Decimal(10**vol_precision)  # 数量精度
    print("数量精度：", precision)
    while True:
        try:
            clientId = client.get_order_id()
            balance = client.balances()
            symbol1, symbol2 = trade_pair.split("_")
            balance1 = Decimal(balance.get(symbol1)['available'])  # SOL
            balance2 = Decimal(balance.get(symbol2)['available'])  # USDC
            print("持币数量：", balance1)
            print("持有USDC数量:", balance2)

            depth = client.depth(trade_pair)
            asks = depth.get("asks")
            bids = depth.get("bids")
            # print(bids, len(bids))
            # print(asks, len(asks))
            bid2 = bids[-2]
            ask2 = asks[1]
            bid_price2 = bid2[0]
            ask_price2 = ask2[0]

            bid_vol2 = bid2[1]
            ask_vol2 = ask2[1]

            if balance1 > trade_quantity * 0.1:
                vol = floor_to(balance1, precision)  # 处理精度.
                order = client.place_order(symbol=trade_pair, side="Ask", order_type="Limit", price=str(bid_price2), quantity=str(vol))
                print("sell position: ", order)

            order = client.place_order(symbol=trade_pair, side="Bid", order_type="Limit", price=str(ask_price2),
                                       quantity=str(trade_quantity))
            print("buy order:", order)

            if order:
                vol = floor_to(trade_quantity * (1-trading_fee), precision)
                order = client.place_order(symbol=trade_pair, side="Ask", order_type="Limit", price=str(bid_price2),
                                           quantity=str(vol))
                print("sell order: ", order)

        except Exception as e:
            print("catch exception: ", e)

        time.sleep(2)
