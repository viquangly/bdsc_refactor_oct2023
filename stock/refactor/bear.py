import stock.refactor.bull as bull
import stock.refactor.strategy as st


class EveningStar(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        current_day_prices = price_indexer.get_standard_prices()
        prior_day_prices = price_indexer.get_standard_prices(-1)
        _2day_prices = price_indexer.get_standard_prices(-2)
        low = min(current_day_prices.low, prior_day_prices.low, _2day_prices.low)

        if not all([
            st.has_uptrend(price_indexer),
            prior_day_prices.open > _2day_prices.close > _2day_prices.open,
            current_day_prices.open < prior_day_prices.close,
            current_day_prices.close < _2day_prices.open
        ]):
            return st.DEFAULT_STRATEGY_RESULT

        prior_day = price_indexer[-1]
        has_doji = bull.Doji().execute(prior_day).pattern
        has_spinning_top = bull.SpinningTop().execute(prior_day).pattern

        if has_doji or has_spinning_top:
            return st.StrategyResult(True, current_day_prices.close, low)

        return st.DEFAULT_STRATEGY_RESULT


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
