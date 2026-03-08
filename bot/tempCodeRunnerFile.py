import logging


def place_market_order(client, symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol = symbol, 
            side = side,
            type = "MARKET",
            quantity = quantity
        )
        logging.info(f"Market order pllaced: {order}")
        print("MARKET ORDER RESPONSE:", order)
        return order
    except Exception as e:
        logging.error(f"Market order failed: {str(e)}")
        print("ERROR:", e)
        return None
    


def place_limit_order(client, symbol,side,quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info(f"Limit order place: {order}")
        print("LIMIT ORDER RESPONSE:", order)
        return order
    except Exception as e:
        logging.error(f"Limit order failed: {str(e)}")
        print("ERROR:", e)
        return None