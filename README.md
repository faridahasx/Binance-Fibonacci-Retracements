# Binance Fibonacci Retracements: Trading Bot and Backtesting Script
The bot live streams 245 USDT pairs and enters a trade when entry conditions are met. 
It also live streams user data so when entry is filled it gives sell order immediately to take profit.

When you enter and exit a trade, you get messages via telegram bot.

## Strategy

        Signal: When high of 1 Hour candlestick is up more than 20% from the opening.
        Fibonacci Retracement levels are calculated based upon open and high of the 1 Hour candlestick.
        
        Entry Level: 0.786
        Exit Level: 0.5
        
        Do not enter a trade second time for the same pair within an hour.


## Backtest 
To test the stategy with different settings and pairs, please refer to ***backtest.ipynb***

## Configure and change the settings of the bot
You can specify how many positions you want to take at once and how much you want to spend for each position.

*To configure the bot, please refer to* **constants.py**

## Set up the telegram bot 
#### 1. Create a chatbot with @BotFather
#### 2.Open terminal and run:
    telegram-send configure


Token telegram-send will ask for the token you got from the botfather and 
then give you a password that you need to message to your new bot on Telegram.

Send the token you got from the botfather and telegram-send will reply with a 5-digit password you need to send to your new bot.
Forward the password to your telegram bot and the bot is ready to send messages to you.



## Run the trading bot
After setting up the bot, run ***bot.py***
