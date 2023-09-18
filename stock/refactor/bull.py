
import stock.refactor.strategy as st


class Marubozu(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        current_day_prices = price_indexer.get_standard_prices()

        if all([
            current_day_prices.close >= current_day_prices.open,
            (current_day_prices.open - current_day_prices.low) <= (current_day_prices.open * 0.01),
            (current_day_prices.close - current_day_prices.high) <= (current_day_prices.close * 0.01)
        ]):
            return st.StrategyResult(True, current_day_prices.close, current_day_prices.low)
        return st.DEFAULT_STRATEGY_RESULT


class SpinningTop(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        current_day_prices = price_indexer.get_standard_prices()

        if current_day_prices.open >= current_day_prices.close:
            upper_shadow = abs(current_day_prices.high - current_day_prices.open)
            lower_shadow = abs(current_day_prices.close - current_day_prices.low)

            pattern = all([
                abs(current_day_prices.open - current_day_prices.close) <= 0.03 * current_day_prices.close,
                abs(upper_shadow - lower_shadow) <= 0.03 * upper_shadow
            ])
        else:
            upper_shadow = abs(current_day_prices.high - current_day_prices.close)
            lower_shadow = abs(current_day_prices.open - current_day_prices.low)

            pattern = (
                (abs(current_day_prices.open - current_day_prices.close) <= 0.03 * current_day_prices.open)
                or (abs(upper_shadow - lower_shadow) <= 0.03 * lower_shadow)
            )

        return st.StrategyResult(pattern, None, None)


class Doji(st.Strategy):

    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        current_day_prices = price_indexer.get_standard_prices()

        pattern = (
            (abs(current_day_prices.open - current_day_prices.close) <= 0.03 * current_day_prices.open)
            or (abs(current_day_prices.open - current_day_prices.close) <= 0.03 * current_day_prices.close)
        )
        return st.StrategyResult(pattern, None, None)


class Hammer(st.Strategy):
    
    def execute(self, price_indexer: st.PriceIndexer) -> st.StrategyResult:
        current_day_prices = price_indexer.get_standard_prices()
        
        if (
                (current_day_prices.open > current_day_prices.close) 
                and (abs(current_day_prices.high - current_day_prices.open) <= (0.02 * current_day_prices.high))
        ):
            body = current_day_prices.open - current_day_prices.close
            lower_shadow = current_day_prices.close - current_day_prices.low
        elif abs(current_day_prices.high - current_day_prices.close) <= (0.02 * current_day_prices.high):
            body = current_day_prices.close - current_day_prices.open
            lower_shadow = current_day_prices.open - current_day_prices.low
        else:
            return st.DEFAULT_STRATEGY_RESULT
        
        if (lower_shadow >= (2 * body)) and st.has_downtrend(price_indexer):
            return st.StrategyResult(True, current_day_prices.close, current_day_prices.low)
        return st.DEFAULT_STRATEGY_RESULT
