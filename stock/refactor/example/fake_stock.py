
from datetime import date, timedelta

import numpy as np
import pandas as pd


def generate_fake_stock_data(n_rows: int) -> pd.DataFrame:
    stock = pd.DataFrame({
        col_name: np.abs(np.random.normal(loc=100, scale=5, size=n_rows)).round(2)
        for col_name in ('Open', 'Close', 'Volume', 'AVG_VOLUME')
    })
    stock['High'] = (stock.max(axis=1) * np.random.uniform(low=1, high=2, size=n_rows)).round(2)
    stock['Low'] = (stock.min(axis=1) * np.random.uniform(low=.5, high=.99, size=n_rows)).round(2)
    stock['Date'] = list(
        reversed([(date.today() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(n_rows)])
    )
    return stock

stock = generate_fake_stock_data(100)
