
from typing import Dict, Sequence

import pandas as pd
import yfinance as yf

from period import Period


def assert_stocks(stocks: Dict[str, Period]) -> None:
    if not isinstance(stocks, dict):
        raise TypeError(
            'stocks must be a dict keyed by str representing stock ticker and Period objs as corresponding values'
        )

    if not all(isinstance(ticker, str) for ticker in stocks):
        raise TypeError('keys in stocks must be str')

    if not all(isinstance(period, Period) for period in stocks.values()):
        raise TypeError('values in stocks must be of type Period')


def _create_ema_feature(data: pd.DataFrame, spans: Sequence[int]) -> None:
    for span in spans:
        data[f'EMA_{span}'] = data["Close"].ewm(span=span, adjust=False).mean()


def _transform_data(data: pd.DataFrame) -> None:
    cols_to_keep = ['Open', 'High', 'Close', 'Low', 'Volume']
    data = data[cols_to_keep]

    _create_ema_feature(data, (50, 100, 9, 21, 200, 25))

    data["MACD"] = (
        data["Close"].ewm(span=12, adjust=False).mean()
        - data["Close"].ewm(span=26, adjust=False).mean()
    )
    data["EMA_MACD"] = data["MACD"].ewm(span=9, adjust=False).mean()
    data["SMA20"] = data["Close"].rolling(window=20).mean()
    data["STD20"] = data["Close"].rolling(window=20).std()
    data["BOL_UP"] = data["SMA20"] + (2 * data["STD20"])
    data["BOL_LOW"] = data["SMA20"] - (2 * data["STD20"])
    data["AVG_VOLUME"] = data["Volume"].rolling(window=10).mean()


class StockData:

    def __init__(self, stocks: Dict[str, Period]):
        assert_stocks(stocks)
        self.stocks = stocks
        self.data_by_stock = None

    def retrieve_data(self):
        self.data_by_stock = {
            ticker: yf.Ticker(ticker).history(period=str(period))
            for ticker, period in self.stocks.items()
        }
        return self

    def transform_data(self) -> pd.DataFrame:
        if self.data_by_stock is None:
            raise ValueError('Must call get_data() method before calling transform_data() method.')
        for data in self.data_by_stock.values():
            _transform_data(data)

        return self.data_by_stock
