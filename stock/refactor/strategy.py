
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Union

import pandas as pd

Numeric = Union[float, int]

StandardPrices = namedtuple('StandardPrices', ['open', 'close', 'high', 'low'])
StrategyResult = namedtuple('StrategyResult', ['pattern', 'price', 'stop_loss'])
DEFAULT_STRATEGY_RESULT = StrategyResult(False, None, None)


class PriceIndexer:

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def __getitem__(self, index: int):
        return self.data.iloc[index]

    def get_price(self, price: str, index: int = -1) -> Numeric:
        return self[index][price]

    def get_previous_price(self, price: str) -> Numeric:
        return self.get_price(price, -2)

    def get_standard_prices(self, index: int = -1) -> StandardPrices:
        out = self[index]
        return StandardPrices(out[price] for price in ('Open', 'Close', 'High', 'Low'))

    def get_previous_standard_prices(self) -> StandardPrices:
        return self.get_standard_prices(-2)


class Strategy(ABC):

    def __init__(self, weight: Numeric):
        self.weight = weight

    @abstractmethod
    def execute(self, price_indexer: PriceIndexer) -> StrategyResult:
        ...
