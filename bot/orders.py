import logging


def place_market_order(client, symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Market order placed: {order}")

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : MARKET")
        print(f"Quantity : {quantity}")

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice')}")

        print("\n✅ Market order placed successfully\n")

        return order

    except Exception as e:
        logging.error(f"Market order failed: {str(e)}")
        print("\n❌ Market order failed")
        print("Error:", e)
        return None



def place_limit_order(client, symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Limit order placed: {order}")

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : LIMIT")
        print(f"Quantity : {quantity}")
        print(f"Price    : {price}")

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice')}")

        print("\n✅ Limit order placed successfully\n")

        return order

    except Exception as e:
        logging.error(f"Limit order failed: {str(e)}")
        print("\n❌ Limit order failed")
        print("Error:", e)
        return None