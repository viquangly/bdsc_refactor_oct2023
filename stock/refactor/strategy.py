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
    prev_day_close = price_indexer.get_price('Close', -2)
    ten_day_close = price_indexer.get_price('Close', -10)
    return (
        (ten_day_close > prev_day_close)
        and (abs(ten_day_close - prev_day_close) >= (0.05 * ten_day_close))
    )


def has_uptrend(price_indexer: PriceIndexer) -> bool:
    prev_day_close = price_indexer.get_price('Close', -2)
    ten_day_close = price_indexer.get_price('Close', -10)
    return (
        (prev_day_close > ten_day_close)
        and (abs(prev_day_close - ten_day_close) >= (0.05 * prev_day_close))
    )


class PriceIndexer:

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def __getitem__(self, index: Union[int, slice]) -> PriceIndexer:
        if isinstance(index, int):
            index = [index]
        return PriceIndexer(self.data.iloc[index])

    def get_row(self, index: int = -1):
        return self.data.iloc[index]

    def get_price(self, price: str, index: int = -1) -> Numeric:
        return self.data.get_row(index)[price]

    def get_standard_prices(self, index: int = -1) -> StandardPrices:
        out = self.get_row(index)
        return StandardPrices(out[price] for price in ('Open', 'Close', 'High', 'Low'))


class Strategy(ABC):

    def __init__(self, weight: Optional[Numeric] = None):
        self.weight = weight

    @abstractmethod
    def execute(self, price_indexer: PriceIndexer) -> StrategyResult:
        ...


class Volume(Strategy):

    def execute(self, price_indexer: PriceIndexer) -> StrategyResult:
        current_day_volume = price_indexer.get_price('Volume')
        current_day_avg_volume = price_indexer.get_price('Avg_Volume')
        return StrategyResult(current_day_volume > current_day_avg_volume, None, None)
