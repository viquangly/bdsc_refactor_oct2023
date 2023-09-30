from copy import deepcopy
from stock.refactor.stock_lot import StockLotLong, StockLotShort, StockLotEMA

default_kwargs = {'price': 100, 'quantity': 100, 'date': '20231004', 'stop_loss': None, 'target': None}
default_ema_kwargs = deepcopy(default_kwargs)
default_ema_kwargs['ema'] = (25, 65)

long0, long1, long2 = (StockLotLong(ticker, **default_kwargs) for ticker in ('Costco', 'BestBuy', 'Wegmans'))
short0, short1, short2 = (StockLotShort(ticker, **default_kwargs) for ticker in ('BMW', 'Toyota', 'Tesla'))
ema0, ema1, ema2 = (StockLotEMA(ticker, **default_ema_kwargs) for ticker in ('Meta', 'TikTok', 'Netflix'))


if __name__ == '__main__':
    long0.get_stock_tag()
    long1.get_stock_tag()
    long2.get_stock_tag()

    short0.get_stock_tag()
    short1.get_stock_tag()
    short2.get_stock_tag()

    ema0.get_stock_tag()
    ema1.get_stock_tag()
    ema2.get_stock_tag()

    ema2.get_unique_id()
    print(ema2)
