
import strategy as st


class Marubozu(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        ...


class SpinningTop(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        ...


class Doji(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        ...


class Hammer(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        ...
