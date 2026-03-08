import argparse

from bot.client import get_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
parser.add_argument("--price", type=float, help="Price for LIMIT order")
args = parser.parse_args()

client = get_client()
side = validate_side(args.side)
order_type = validate_order_type(args.type)


if order_type == "MARKET":
    place_market_order(client, args.symbol, side, args.quantity)
elif order_type == "LIMIT":
    if args.price is None:
        print("Price is required for LIMIT order")
    else:
        place_limit_order(client, args.symbol, side, args.quantity, args.price)