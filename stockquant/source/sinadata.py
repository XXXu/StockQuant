import requests
from stockquant.tick import Tick


class SinaData:

    def __init__(self):
        pass

    @staticmethod
    def check_digit_start(str):
        if not str:  # 检查字符串是否为空
            return False
        first_char = str[0]
        if first_char.isalpha():
            return False
        elif first_char.isdigit():
            return True

    @staticmethod
    def get_stock_exchange(code):
        code_str = str(code)
        prefix = ""
        if code_str.startswith(('600', '601', '603', '605')):
            prefix = 'sh'  # 上海证券交易所
        elif code_str.startswith(('000', '001', '002', '003', '300', '301')):
            prefix = 'sz'  # 深圳证券交易所
        elif code_str.startswith('688'):
            prefix = 'sh'  # 科创板
        elif code_str.startswith('8'):
            prefix = 'bj'  # 北京证券交易所
        elif code_str.startswith('4'):
            prefix = 'bj'  # 北京证券交易所
        else:
            prefix = ""  # 未知交易所
        symbol = f"{prefix}{code}"
        return symbol

    @staticmethod
    def get_realtime_data(symbol):
        """
        获取指定股票的实时数据
        :param symbol: 例如："sh601003"，或者"sz002307"，前者是沪市，后者是深市
        :return:返回一个字典
        """
        if SinaData.check_digit_start(symbol):
            symbol = SinaData.get_stock_exchange(symbol)
        url = f"https://hq.sinajs.cn/list={symbol}"
        headers = {
            'Referer': 'https://finance.sina.com.cn'
        }
        response = requests.get(url, headers=headers).text

        tick = Tick()
        data = response.split(",")
        tick.symbol = symbol
        tick.name = data[0].split('"')[1]
        tick.timestamp = data[-4] + " " + data[-3] if str(symbol).startswith("sh") else data[-3] + " " + data[-2]
        tick.open_price = float(data[1])                    # 今日开盘价
        tick.yesterday_close = float(data[2])         # 昨日收盘价
        tick.current_price = float(data[3])           # 当前价格
        tick.high_price = float(data[4])                    # 今日最高价
        tick.low_price = float(data[5])                     # 今日最低价
        tick.bid_price = float(data[6])               # 竞买价
        tick.ask_price = float(data[7])               # 竞卖价
        tick.transactions = round(float(data[8]))     # 成交数量
        tick.turnover = round(float(data[9]))         # 成交金额
        tick.bid1_quantity = round(float(data[10]))   # 买一数量
        tick.bid1_price = float(data[11])             # 买一报价
        tick.ask1_quantity = round(float(data[20]))   # 卖一数量
        tick.ask1_price = float(data[21])             # 卖一报价
        tick.updown = round(tick.current_price - tick.yesterday_close, 2)
        tick.percent = round((tick.updown/tick.yesterday_close)*100, 2)

        return tick

    @staticmethod
    def shenzhen_component_index():
        """
        获取深圳成指
        :return:返回一个字典
        """
        url = "https://hq.sinajs.cn/list=sz399001"
        headers = {
            'Referer': 'https://finance.sina.com.cn'
        }
        response = requests.get(url, headers=headers).text
        data = response.split(",")

        open_price = round(float(data[1]), 2)
        prev_close = round(float(data[2]), 2)
        current_price = round(float(data[3]), 2)
        high_price = round(float(data[4]), 2)
        low_price = round(float(data[5]), 2)
        updown = round(float(current_price) - float(prev_close), 2)
        percent = round((updown / prev_close) * 100, 2)
        transactions = round(float(data[8]), 2)
        turnover = round(float(data[9]), 2)

        result = {
            "指数名称": data[0].replace('"', "").split("=")[1],
            "今开点数": open_price,
            "昨收点数": prev_close,
            "当前点数": current_price,
            "最高点数": high_price,
            "最低点数": low_price,
            "涨跌点数": updown,
            "涨跌率": percent,
            "成交数量": transactions,
            "成交金额": turnover
        }
        return result

    @staticmethod
    def shanghai_component_index():
        """
        获取上证综指
        :return:
        """
        url = "https://hq.sinajs.cn/list=sh000001"
        headers = {
            'Referer': 'https://finance.sina.com.cn'
        }
        response = requests.get(url, headers=headers).text
        data = response.split(",")
        open_price = round(float(data[1]),2)
        prev_close = round(float(data[2]),2)
        current_price = round(float(data[3]),2)
        high_price = round(float(data[4]),2)
        low_price = round(float(data[5]),2)
        updown = round(float(current_price) - float(prev_close),2)
        percent = round((updown/prev_close)*100, 2)
        transactions = round(float(data[8]),2)
        turnover = round(float(data[9]),2)
        result = {
            "指数名称": data[0].replace('"', "").split("=")[1],
            "今开点数": open_price,
            "昨收点数": prev_close,
            "当前点数": current_price,
            "最高点数": high_price,
            "最低点数": low_price,
            "涨跌点数": updown,
            "涨跌率": percent,
            "成交数量": transactions,
            "成交金额": turnover
        }
        return result

if __name__ == '__main__':
    print(SinaData.get_realtime_data("300927"))
    print(SinaData.get_realtime_data("688630"))
    print(SinaData.get_realtime_data("870508"))
    print(SinaData.get_realtime_data("430489"))
    print(SinaData.get_realtime_data("600105"))
    print(SinaData.get_realtime_data("688298"))

    sh = SinaData.shanghai_component_index()
    print(sh)

    sz = SinaData.shenzhen_component_index()
    print(sz)