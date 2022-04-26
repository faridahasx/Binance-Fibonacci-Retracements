"""
Strategy

Signal: When high of 1 Hour candlestick is up more than 20% from the opening.
Fibonacci Retracement levels are calculated based upon open and high of the candlestick.

Entry Level: 0.786
Exit Level: 0.5

Entry:If you don't have an open position, give limit buy order after the signal.
If were you already in position and you exit the position before the price drops to the entry level of current signal, give limit buy order.

Exit: Give limit sell order right after the entry and wait until the order is filled.


The bot will get live prices for each USDT pair listed in Binance and get in trade

To change the settings of the bot, please refer to constants.py file

"""


import logging
import websocket
import json
import ccxt
import threading
import warnings
from datetime import datetime as dt
from binance.client import Client
from ws_functions import on_close, on_open, on_ping, on_pong, on_error
import telegram_send
from constants import *

logging.basicConfig(level=logging.INFO, filename='bot.log', format='%(asctime)s:%(levelname)s:%(message)s', )

warnings.filterwarnings('ignore')
exchange = ccxt.binance({
    'options': {
        'adjustForTimeDifference': True,
        'recvWindow': 50000,
    },
    'enableRateLimit': True,
    'apiKey': API_KEY,
    'secret': API_SECRET,
})
exchange.load_markets()
client = Client(api_key=API_KEY, api_secret=API_SECRET, tld='com')

filled_entries = {}
buy_orders = {}
sell_orders = {}
order_ids = []


def on_message(ws, message):
    global buy_orders, sell_orders, filled_entries
    global order_ids
    json_array = json.loads(message)
    pair = json_array['s']
    opening = float(json_array['o'])
    high = float(json_array['h'])
    close = float(json_array['c'])

    # If high is 20% more than low and current price is more than opening
    if opening * GAIN <= high and close > opening:

        # Calculate entry and exit price
        entry_price = high - ((high - opening) * ENTRY_LEVEL)
        exit_price = high - ((high - opening) * EXIT_LEVEL)

        # Give buy order when price is 1% upper than entry level
        if close <= entry_price * 1.01:

            # If pair was not in position in the current hour
            now = dt.now()
            if pair not in filled_entries or (pair in filled_entries and (now - filled_entries[pair]).hour > 0):

                # If buy orders + sell orders < position limit
                if len(buy_orders) + len(sell_orders) < position_limit:

                    # If current price is less than the entry price, change entry price to current price
                    if close < entry_price:
                        entry_price = close

                    try:
                        # Calculate decimal precision
                        buy_amount = exchange.amount_to_precision(symbol=pair, amount=USDT_to_spend / entry_price)
                        buy_price = exchange.price_to_precision(symbol=pair, price=entry_price)

                        # Check if total USDT to spend is more than 10 after calculating decimal precision
                        if float(buy_amount) * float(buy_price) > 10:

                            # Give buy order
                            buy_order = exchange.create_limit_buy_order(symbol=pair, price=buy_price,
                                                                        amount=buy_amount)
                            # Track the order
                            buy_orders[pair] = {'exit price': exit_price}
                            order_ids.append(int(buy_order['id']))

                            # Info
                            logging.info(f'BUY ORDER: {pair}')
                            telegram_send.send(messages=[f'BUY ORDER: {pair}, ENTRY: {buy_price}, EXIT: {exit_price}'])

                    except Exception as e:
                        logging.error(f'Buy Error:{pair}, {e}')
                        telegram_send.send(messages=[f'Buy Error:{pair}, {e}'])

            # Don't let pair enter a second trade in an hour
            filled_entries[pair] = now


def user_data_stream():
    while True:
        key = client.stream_get_listen_key()

        socket = f'wss://stream.binance.com:9443/ws/{key}'

        def on_message(ws, message):
            global order_ids, buy_orders, sell_orders

            json_array = json.loads(message)

            if json_array['e'] == 'executionReport':
                order_id = json_array['i']

                if order_id in order_ids:
                    side = json_array['S']
                    symbol = json_array['s']
                    status = json_array['X']
                    executed_quantity = float(json_array['z'])

                    if side == 'BUY' and status == 'FILLED':
                        price = buy_orders[symbol]['exit price']
                        entry_price = float(json_array['p'])

                        # Give Limit Sell Order
                        try:
                            sell_amount = exchange.amount_to_precision(symbol=symbol, amount=executed_quantity)
                            sell_price = exchange.price_to_precision(symbol=symbol, price=price)
                            sell_order = exchange.create_limit_sell_order(symbol=symbol, amount=sell_amount,
                                                                          price=sell_price)
                            profit = (price - entry_price) * 100 / entry_price
                            sell_orders[symbol] = {'take profit': profit}
                            buy_orders.pop(symbol)
                            logging.info(f'FILLED BUY ORDER: {symbol}, SELL ORDER TAKE PROFIT: {round(profit, 3)}%')
                            telegram_send.send(
                                messages=[f'FILLED BUY ORDER: {symbol}, SELL ORDER TAKE PROFIT: {round(profit, 3)}%'])
                            order_ids.append(int(sell_order['id']))

                        except Exception as e:
                            sell_amount = exchange.amount_to_precision(symbol=symbol, amount=executed_quantity)
                            sell_price = exchange.price_to_precision(symbol=symbol, price=price)
                            logging.error(f'SELL ERROR: {symbol} - - {e}')
                            telegram_send.send(messages=[f'SELL ERROR: {symbol} - - {e}, {sell_price} - {sell_amount}'])
                        order_ids.remove(order_id)

                    elif side == 'SELL' and status == 'FILLED':
                        profit = sell_orders[symbol]['take profit']
                        sell_orders.pop(symbol)
                        order_ids.remove(order_id)
                        telegram_send.send(messages=[f'FILLED SELL ORDER: {symbol}, PROFIT: {round(profit, 3)}%'])
                        logging.info(f'FILLED SELL ORDER: {symbol}, PROFIT: {round(profit, 3)}%')

                    elif side == 'SELL' and status == 'CANCELED':
                        logging.info(f'CANCELED SELL ORDER: {symbol}')
                        sell_orders.pop(symbol)
                        telegram_send.send(messages=[f'CANCELED SELL ORDER: {symbol}'])
                        order_ids.remove(order_id)

                    elif side == 'BUY' and status == 'CANCELED':
                        logging.info(f'CANCELED BUY ORDER: {symbol}')
                        buy_orders.pop(symbol)
                        telegram_send.send(messages=[f'CANCELED BUY ORDER: {symbol}'])
                        order_ids.remove(order_id)

        ws = websocket.WebSocketApp(socket, on_open=on_open, on_close=on_close, on_message=on_message,
                                    on_error=on_error,
                                    on_ping=on_ping, on_pong=on_pong)

        ws.run_forever()


def connect(on_message, socket):
    ws = websocket.WebSocketApp(socket, on_open=on_open,
                                on_close=on_close,
                                on_message=on_message, on_error=on_error,
                                on_ping=on_ping, on_pong=on_pong)
    while True:
        ws.run_forever()


if __name__ == '__main__':
    logging.info("Bot Started...")
    telegram_send.send(messages=["Fibonacci Bot Started..."])

    threads = []

    thread = threading.Thread(target=connect, args=(on_message, SOCKET))
    thread.start()
    threads.append(thread)
    threads.append(thread)

    thread1 = threading.Thread(target=user_data_stream, args=())
    thread1.start()
    threads.append(thread1)
    threads.append(thread1)

    for t in threads:
        t.join()
