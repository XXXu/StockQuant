from dataclasses import dataclass


@dataclass(init=False)
class Tick:
    def __init__(self):
        self.percent = 0.0
        self.updown = 0.0
        self.ask1_quantity = 0
        self.ask1_price = 0.0
        self.bid1_quantity = 0
        self.bid1_price = 0.0
    """ 实时行情数据"""
    symbol: str                             # 股票代码
    name: str                               # 股票名称
    percent: float                          # 涨跌幅度
    updown: float                           # 涨跌点数
    open_price: float                       # 今日开盘价
    yesterday_close: float                  # 昨日收盘价
    current_price: float                    # 当前价格
    high_price: float                       # 今日最高价
    low_price: float                        # 今日最低价
    bid_price: float                        # 竞买价
    ask_price: float                        # 竞卖价
    transactions: int                       # 成交数量
    turnover: float                         # 成交金额
    bid1_quantity: int                      # 买一数量
    bid1_price: float                       # 买一报价
    ask1_quantity: int                      # 卖一数量
    ask1_price: float                       # 卖一报价
    timestamp: str                          # 时间戳