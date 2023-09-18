
from abc import ABC, abstractmethod
import bisect
from typing import Sequence

import stock.refactor.strategy as st
import stock.refactor.bull as bull
import stock.refactor.bear as bear


def calculate_cash(
        x, max_cash: st.Numeric = .15,
        long_shorts: Sequence[st.Numeric] = (.2, .3, .4, .5, .6, .7, .8),
        cash: Sequence[st.Numeric] = (.05, .06, .07, .08, .09, .1, .11)
) -> st.Numeric:
    if x > long_shorts[-1]:
        return max_cash
    index = bisect.bisect_left(long_shorts, x)
    return cash[index]


class Call(ABC):

    @abstractmethod
    def __init__(self, strategies: Sequence[st.Strategy]):
        self.strategies = strategies

    def calculate_cash(self, price_indexer: st.PriceIndexer) -> st.Numeric:
        lookup_value = 0
        for strategy in self.strategies:
            result = strategy.execute(price_indexer)
            if result.pattern:
                lookup_value += strategy.weight

        return calculate_cash(lookup_value)


class LongCall(Call):

    def __init__(self):
        super().__init__(
            (bull.Marubozu(.1), bull.SpinningTop(.2), bull.Doji(.3), bull.Hammer(.35), st.Volume(.5))
        )


class ShortCall(Call):

    def __init__(self):
        super().__init__(
            (bear.Marubozu(.1), bear.SpinningTop(.2), bear.Doji(.3), bear.Hammer(.35), st.Volume(.5))
        )
