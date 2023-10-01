
from copy import deepcopy
from datetime import date, timedelta, datetime
import itertools
from typing import Collection, Dict

import numpy as np
import pandas as pd

from stock.refactor.stock_lot import StockLot, StockLotShort, StockLotEMA, StockLotLong


def generate_fake_stock_data(ticker: str, n_rows: int = 100) -> pd.DataFrame:
    stock = pd.DataFrame({
        col_name: np.abs(np.random.normal(loc=100, scale=5, size=n_rows)).round(2)
        for col_name in ('Open', 'Close', 'Volume', 'AVG_VOLUME')
    })
    stock['High'] = (stock.max(axis=1) * np.random.uniform(low=1, high=2, size=n_rows)).round(2)
    stock['Low'] = (stock.min(axis=1) * np.random.uniform(low=.5, high=.99, size=n_rows)).round(2)
    stock['Date'] = list(
        reversed([(date.today() - timedelta(days=x)).strftime('%Y%m%d') for x in range(n_rows)])
    )
    stock['Ticker'] = ticker
    return stock.set_index('Date')


def create_stocks_lookup(lots: Collection[StockLot]) -> Dict:
    return {lot.stock: generate_fake_stock_data(lot.stock) for lot in lots}


default_kwargs = {
    'price': 100, 'quantity': 100, 'date': datetime.today().strftime('%Y%m%d'), 'stop_loss': None, 'target': None
}
default_ema_kwargs = deepcopy(default_kwargs)
default_ema_kwargs['ema'] = (25, 65)

long_lots = [StockLotLong(ticker, **default_kwargs) for ticker in ('Costco', 'BestBuy', 'Wegmans')]
short_lots = [StockLotShort(ticker, **default_kwargs) for ticker in ('BMW', 'Toyota', 'Tesla')]
ema_lots = [StockLotEMA(ticker, **default_ema_kwargs) for ticker in ('Meta', 'TikTok', 'Netflix')]

all_lots = list(itertools.chain(long_lots, short_lots, ema_lots))
stocks_lookup = create_stocks_lookup(all_lots)
