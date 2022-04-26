import logging
import telegram_send

logging.basicConfig(level=logging.INFO, filename='bot.log', format='%(asctime)s:%(levelname)s:%(message)s', )


def on_open(ws):
    logging.info("Opened connection")
    telegram_send.send(messages=["Opened Connection!"])



def on_close(ws, close_status_code, close_msg):
    logging.critical("Closed connection")
    telegram_send.send(messages=["Closed connection"])

def on_error(ws, error):
    logging.error(error)
    telegram_send.send(messages=[str(error)])

def on_ping(wsapp, message):
    pass


def on_pong(wsapp, message):
    pass
