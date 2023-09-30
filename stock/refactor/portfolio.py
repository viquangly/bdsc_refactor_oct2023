
import itertools
from typing import Dict, List, Set

from stock.refactor.strategy import Numeric
from stock.original.updated_algo import Stock_Lot_Short, Stock_Lot_EMA, Stock_Lot_Long


def _get_worth(stocks: Dict, date: str, lots: List) -> Numeric:
    worth = 0
    for lot in lots:
        stock_data = stocks[lot.stock]
        stock_worth = stock_data.at[date, "Close"]
        worth += stock_worth * lot.quanity
    return worth


class PortfolioWithDict:

    def __init__(self, long_cash: Numeric, short_cash: Numeric, stock_lots: Dict):
        self.long_cash = long_cash
        self.short_cash = short_cash
        self.stock_lots = stock_lots

    def add(self, lot):
        for key, lot_type in (
                ('EMA', Stock_Lot_EMA), ('Short', Stock_Lot_Short), ('Long', Stock_Lot_Long)
        ):
            if isinstance(lot, lot_type):
                self.stock_lots[key].append(lot)
                return None
        raise TypeError('lot must be an object of type Stock_Lot_EMA, Stock_Lot_Short, or Stock_Lot_Long')

    def remove(self, lot):
        for key, lot_type in (
                ('EMA', Stock_Lot_EMA), ('Short', Stock_Lot_Short), ('Long', Stock_Lot_Long)
        ):
            if isinstance(lot, lot_type):
                self.stock_lots[key].remove(lot)
                return None
        raise TypeError('lot must be an object of type Stock_Lot_EMA, Stock_Lot_Short, or Stock_Lot_Long')

    def get_short_worth(self, stocks_lookup: Dict, date: str):
        valid_lots = self.stock_lots['Short']
        return _get_worth(stocks_lookup, date, valid_lots)

    def get_long_worth(self, stocks_lookup: Dict, date: str):
        valid_lots = [lots for key, lots in self.stock_lots.items() if key != 'Short']
        valid_lots = list(itertools.chain(*valid_lots))
        return _get_worth(stocks_lookup, date, valid_lots)


class PortfolioWithList:

    def __init__(self, long_cash: Numeric, short_cash: Numeric, stock_lots: List):
        self.long_cash = long_cash
        self.short_cash = short_cash
        self.stock_lots = stock_lots

    def add(self, lot):
        self.stock_lots.append(lot)

    def remove(self, lot):
        self.stock_lots.remove(lot)

    def get_short_worth(self, stocks_lookup: Dict, date: str):
        valid_lots = [lot for lot in self.stock_lots if isinstance(lot, Stock_Lot_Short)]
        return _get_worth(stocks_lookup, date, valid_lots)

    def get_long_worth(self, stocks_lookup: Dict, date: str):
        valid_lots = [lot for lot in self.stock_lots if not isinstance(lot, Stock_Lot_Short)]
        return _get_worth(stocks_lookup, date, valid_lots)

    def print_portfolio(self):

        print("---------------------------------")
        for lot in self.stock_lots:
            print(lot)

        print(f"Cash: ${self.long_cash:,.2f}")
        print("---------------------------------")


class PortfolioWithSet:

    def __init__(self, long_cash: Numeric, short_cash: Numeric, stock_lots: Set):
        self.long_cash = long_cash
        self.short_cash = short_cash
        self.stock_lots = stock_lots

    def add(self, lot):
        self.stock_lots.add(lot)

    def remove(self, lot):
        self.stock_lots.remove(lot)

    def get_short_worth(self, stocks_lookup: Dict, date: str):
        valid_lots = [lot for lot in self.stock_lots if isinstance(lot, Stock_Lot_Short)]
        return _get_worth(stocks_lookup, date, valid_lots)

    def get_long_worth(self, stocks_lookup: Dict, date: str):
        valid_lots = [lot for lot in self.stock_lots if not isinstance(lot, Stock_Lot_Short)]
        return _get_worth(stocks_lookup, date, valid_lots)

    def print_portfolio(self):

        print("---------------------------------")
        for lot in self.stock_lots:
            print(lot)

        print(f"Cash: ${self.long_cash:,.2f}")
        print("---------------------------------")
