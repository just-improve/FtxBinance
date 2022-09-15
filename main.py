from M2 import M2bot
import signal
import time
import sys

from M2_binance import M2bot_binance

year_in_seconds = 31556926
fifteen_days_in_seconds = 1296000
ten_days_in_seconds = 864000
one_day_in_seconds = 86400
one_hour_in_seconds = 3600
ten_minutes_in_seconds = 600
RESOLUTION = {"1m": 60, "5m": 300, "1h": 3600, "1d": 86400, "10d":864000, "15d":1296000}
list_of_oi= []
list_of_fr = []
fee_ftx_market_bet = 0.00064505
gap_reverse_long = 1.015
gap_reverse_short = 0.985
gap_profit_long = 1.05
gap_profit_short = 0.95
refresh_time = 5


if __name__ == '__main__':

    #market_bot_btc = MarketBotClass("BTC-PERP")
    obj = M2bot("CEL-PERP",fee_ftx_market_bet, gap_reverse_long, gap_reverse_short, gap_profit_long, gap_profit_short, refresh_time)   #
    obj.start_bot()
    #obj_binance = M2bot_binance("ADAUSDT")
    #pass



#czemu sie wywoluje klasa test i cały kod wszystkich klas?