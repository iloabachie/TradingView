from tradingview_ta import TA_Handler, Exchange, Interval
from datetime import datetime, date

# https://tvdb.brianthe.dev/

SYMBOLS = ['EURUSD', 'EURGBP', 'EURJPY', 'EURCHF', 'EURAUD', 'EURCAD', 'USDJPY', 'USDCAD', 'USDCHF', 'GBPUSD', 'GBPJPY', 'GBPCAD', 'CADCHF', 'CHFJPY', 'AUDUSD', 'AUDCAD', 'AUDJPY', 'AUDCHF', 'NZDJPY']

def trade_analysis(symbol, screener='forex', exchange='FX_IDC'):
    global INTERVAL
    INTERVAL = [Interval.INTERVAL_1_MINUTE, 
                Interval.INTERVAL_5_MINUTES, 
                Interval.INTERVAL_15_MINUTES, 
                Interval.INTERVAL_30_MINUTES, 
                Interval.INTERVAL_1_HOUR, 
                Interval.INTERVAL_2_HOURS, 
                Interval.INTERVAL_4_HOURS, 
                Interval.INTERVAL_1_DAY, 
                Interval.INTERVAL_1_WEEK, 
                Interval.INTERVAL_1_MONTH]

    recommendations = dict()

    for time_frame in INTERVAL:   
        handler = TA_Handler(symbol=symbol, screener=screener,exchange=exchange, interval=time_frame)
        recommendations[time_frame] = handler.get_analysis().summary

    return recommendations


if __name__ == '__main__':  
    r = 'RECOMMENDATION'
    b = 'BUY' 
    s = 'SELL'
    n = 'NEUTRAL'
  
    for symbol in SYMBOLS:
        rec = trade_analysis(symbol)
        print("\033[94m+----------+-----+-------------+-----+------+---------+----------+")
        print("| Symbol   | Int | Recommend   | Buy | Sell | Neutral | Date     |")
        print("+----------+-----+-------------+-----+------+---------+----------+\033[0m")   
        for intr in INTERVAL:
            reco = rec[intr][r]
            if "BUY" in reco:
                color = "\033[32m"
            elif "SELL" in reco:
                color = "\033[31m"
            else:
                color = "\033[33m"
            print(f"| {symbol:8} | {intr:3} | {color}{reco:11}\033[0m | {rec[intr][b]:>3d} | {rec[intr][s]:>4d} | {rec[intr][n]:>7d} | {datetime.now():%H:%M:%S} |")
            print("+----------+-----+-------------+-----+------+---------+----------+")  
            if intr == '1M':
                print()
        
