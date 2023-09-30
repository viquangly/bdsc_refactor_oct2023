from copy import deepcopy
from datetime import datetime
from stock.refactor.stock_lot import StockLotLong, StockLotShort, StockLotEMA

default_kwargs = {
    'price': 100, 'quantity': 100, 'date': datetime.today().strftime('%Y%m%d'), 'stop_loss': None, 'target': None
}
default_ema_kwargs = deepcopy(default_kwargs)
default_ema_kwargs['ema'] = (25, 65)

long_lots = [StockLotLong(ticker, **default_kwargs) for ticker in ('Costco', 'BestBuy', 'Wegmans')]
short_lots = [StockLotShort(ticker, **default_kwargs) for ticker in ('BMW', 'Toyota', 'Tesla')]
ema_lots = [StockLotEMA(ticker, **default_ema_kwargs) for ticker in ('Meta', 'TikTok', 'Netflix')]

if __name__ == '__main__':
    long_lots[0].get_stock_tag()
    long_lots[1].get_stock_tag()
    long_lots[2].get_stock_tag()

    short_lots[0].get_stock_tag()
    short_lots[1].get_stock_tag()
    short_lots[2].get_stock_tag()

    ema_lots[0].get_stock_tag()
    ema_lots[1].get_stock_tag()
    ema_lots[2].get_stock_tag()

    ema_lots[2].get_unique_id()
    print(ema_lots[2])
