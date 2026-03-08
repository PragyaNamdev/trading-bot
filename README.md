# Binance Futures Testnet Trading Bot

A simple CLI-based trading bot built with Python that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY / SELL support
- CLI input validation
- Logging of API requests and responses
- Error handling

## Project Structure

trading_bot/
  bot/
    client.py
    orders.py
    validators.py
    logging_config.py
  cli.py
  requirements.txt
  README.md

## Setup Instructions

1. Clone the repository

git clone https://github.com/yourusername/trading_bot.git

2. Navigate to project folder

cd trading_bot

3. Create virtual environment

python -m venv venv

4. Activate environment

Windows:
venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Add Binance Testnet API Keys

Edit `bot/client.py`

API_KEY="YOUR_API_KEY"
API_SECRET="YOUR_SECRET_KEY"

## Example Usage

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### LIMIT Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000

## Logs

Logs are stored in:

bot.log

Logs contain:
- API requests
- API responses
- Errors

## Assumptions

- Binance Futures Testnet account is active
- USDT-M Futures API permissions enabled
- Symbol exists on testnet
