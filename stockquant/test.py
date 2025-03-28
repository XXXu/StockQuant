from stockquant.quant import *
config.loads("config.json")


def test_000():
    tick = Market.tick("sh601003")
    content = "### 交易提醒之股票实时行情推送\n\n"\
              "> **股票代码：** {symbol}\n\n"\
              "> **股票名称：** {name}\n\n"\
              "> **当前价格：** {current_price}\n\n"\
              "> **涨跌幅度：** {percent}\n\n"\
              "> **涨跌点数：** {updown}\n\n"\
              "> **今日开盘价：** {open_price}\n\n"\
              "> **今日最高价：** {high_price}\n\n"\
              "> **今日最低价：** {low_price}\n\n"\
              "> **昨日收盘价：** {yesterday_close}\n\n"\
              "> **竞买价：** {bid_price}\n\n"\
              "> **竞卖价：** {ask_price}\n\n"\
              "> **当前时间：** {timestamp}".format(symbol=tick.symbol, name=tick.name, current_price=tick.current_price, percent=tick.percent,
                                                   updown=tick.updown, open_price=tick.open_price, high_price=tick.high_price, low_price=tick.low_price,
                                                   yesterday_close=tick.yesterday_close, bid_price=tick.bid_price, ask_price=tick.ask_price, timestamp=tick.timestamp)
    DingTalk.markdown(content)
def test_001():
    print(Market.tick("sh601003"))
    kline = Market.kline("sh601003", "1d", start_date="2023-03-01", end_date="2025-03-27")
    print("kline is: ", kline)
    macd = MACD(14, 26, 9, kline=kline)
    print("macd is: ",macd)
    kdj = KDJ(20, 30, 9, kline=kline)
    print("kdj is: ", kdj)


if __name__ == "__main__":
    test_001()