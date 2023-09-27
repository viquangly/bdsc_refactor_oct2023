from __future__ import annotations
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Union, Optional

import pandas as pd

Numeric = Union[float, int]

StandardPrices = namedtuple('StandardPrices', ['open', 'close', 'high', 'low'])
StrategyResult = namedtuple('StrategyResult', ['pattern', 'price', 'stop_loss'])
DEFAULT_STRATEGY_RESULT = StrategyResult(False, None, None)


def has_downtrend(price_indexer: PriceIndexer) -> bool:
    prev_day_close = price_indexer.get_price('Close', -1)
    _9day_ago_close = price_indexer.get_price('Close', -9)
    return (
        (_9day_ago_close > prev_day_close)
        and (abs(_9day_ago_close - prev_day_close) >= (0.05 * _9day_ago_close))
    )


def has_uptrend(price_indexer: PriceIndexer) -> bool:
    prev_day_close = price_indexer.get_price('Close', -1)
    _9day_ago_close = price_indexer.get_price('Close', -9)
    return (
        (prev_day_close > _9day_ago_close)
        and (abs(prev_day_close - _9day_ago_close) >= (0.05 * prev_day_close))
    )


class PriceIndexer:

    def __init__(self, data: pd.DataFrame):
        self.data = data

    @staticmethod
    def _shift_index(index: int) -> int:
        if index > 0:
            raise ValueError('index must be <= 0 when given an int')
        shift_for_zero_index = 1
        return index - shift_for_zero_index

    def __getitem__(self, index: Union[int, slice]) -> PriceIndexer:
        if isinstance(index, int):
            return PriceIndexer(self.get_row(index, as_dataframe=True))

        new_slice_args = [None if x is None else self._shift_index(x) for x in (index.start, index.stop, index.step)]
        new_slice = slice(*new_slice_args)
        return PriceIndexer(self.data.iloc[new_slice])

    def get_row(self, index: int = 0, as_dataframe: bool = False) -> Union[pd.Series, pd.DataFrame]:
        index = self._shift_index(index)
        return self.data.iloc[[index]] if as_dataframe else self.data.iloc[index]

    def get_price(self, price: str, index: int = 0) -> Numeric:
        return self.get_row(index)[price]

    def get_standard_prices(self, index: int = 0) -> StandardPrices:
        out = self.get_row(index)
        return StandardPrices(*[out[price] for price in ('Open', 'Close', 'High', 'Low')])


class Strategy(ABC):

    def __init__(self, weight: Numeric = 0):
        self.weight = weight

    @abstractmethod
    def execute(self, price_indexer: PriceIndexer) -> StrategyResult:
        ...


class Volume(Strategy):

    def execute(self, price_indexer: PriceIndexer) -> StrategyResult:
        current_day_volume = price_indexer.get_price('Volume')
        current_day_avg_volume = price_indexer.get_price('AVG_VOLUME')
        return StrategyResult(current_day_volume > current_day_avg_volume, None, None)
