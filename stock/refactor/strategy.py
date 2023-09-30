from __future__ import annotations
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Union

import pandas as pd

from _typing import Numeric

StandardPrices = namedtuple('StandardPrices', ['open', 'close', 'high', 'low'])
StrategyResult = namedtuple('StrategyResult', ['pattern', 'price', 'stop_loss'])
DEFAULT_STRATEGY_RESULT = StrategyResult(False, None, None)


def has_downtrend(price_indexer: PriceRetriever) -> bool:
    prev_day_close = price_indexer.get_price('Close', -1)
    _9day_ago_close = price_indexer.get_price('Close', -9)
    return (
        (_9day_ago_close > prev_day_close)
        and (abs(_9day_ago_close - prev_day_close) >= (0.05 * _9day_ago_close))
    )


def has_uptrend(price_indexer: PriceRetriever) -> bool:
    prev_day_close = price_indexer.get_price('Close', -1)
    _9day_ago_close = price_indexer.get_price('Close', -9)
    return (
        (prev_day_close > _9day_ago_close)
        and (abs(prev_day_close - _9day_ago_close) >= (0.05 * prev_day_close))
    )


class PriceRetriever:

    def __init__(self, data: pd.DataFrame):
        self.data = data

    @staticmethod
    def _shift_index(index: int) -> int:
        if index > 0:
            raise ValueError('index must be <= 0 when given an int')
        shift_for_zero_index = 1
        return index - shift_for_zero_index

    def __getitem__(self, index: Union[int, slice]) -> PriceRetriever:
        if isinstance(index, int):
            return PriceRetriever(self.get_row(index, as_dataframe=True))

        start, stop = [None if x is None else self._shift_index(x) for x in (index.start, index.stop)]
        new_slice = slice(start, stop, index.step)
        return PriceRetriever(self.data.iloc[new_slice])

    def get_row(self, days_ago: int = 0, as_dataframe: bool = False) -> Union[pd.Series, pd.DataFrame]:
        days_ago = self._shift_index(days_ago)
        return self.data.iloc[[days_ago]] if as_dataframe else self.data.iloc[days_ago]

    def get_price(self, metric: str, days_ago: int = 0) -> Numeric:
        return self.get_row(days_ago)[metric]

    def get_standard_prices(self, days_ago: int = 0) -> StandardPrices:
        out = self.get_row(days_ago)
        return StandardPrices(*[out[price] for price in ('Open', 'Close', 'High', 'Low')])


class Strategy(ABC):

    def __init__(self, weight: Numeric = 0):
        self.weight = weight

    @abstractmethod
    def execute(self, price_indexer: PriceRetriever) -> StrategyResult:
        ...


class Volume(Strategy):

    def execute(self, price_indexer: PriceRetriever) -> StrategyResult:
        current_day_volume = price_indexer.get_price('Volume')
        current_day_avg_volume = price_indexer.get_price('AVG_VOLUME')
        return StrategyResult(current_day_volume > current_day_avg_volume, None, None)
