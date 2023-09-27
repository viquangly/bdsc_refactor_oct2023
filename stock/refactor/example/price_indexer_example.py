
from datetime import date, timedelta

import numpy as np
import pandas as pd

from stock.refactor.strategy import PriceIndexer


def generate_fake_stock_data(n_rows: int) -> pd.DataFrame:
    stock = pd.DataFrame({
        col_name: np.abs(np.random.normal(loc=100, scale=5, size=n_rows)).round(2) for col_name in ('Open', 'Close')
    })
    stock['High'] = (stock.max(axis=1) * np.random.uniform(low=1, high=2, size=n_rows)).round(2)
    stock['Low'] = (stock.min(axis=1) * np.random.uniform(low=.5, high=.99, size=n_rows)).round(2)
    stock['Date'] = list(
        reversed([(date.today() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(n_rows)])
    )
    return stock


stock = generate_fake_stock_data(100)
stock_index = PriceIndexer(stock)

stock.iloc[-1]
stock_index.get_row(0)

stock.iloc[-2]
stock_index.get_price('High', -1)

stock_index[-1]
stock_index[-1].data

stock_index[0]
stock_index[0].data

stock_index[-2:].data