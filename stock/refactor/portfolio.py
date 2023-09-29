
from typing import Dict, List

from stock.refactor.strategy import Numeric
from stock.original.updated_algo import Stock_Lot_Short


def _get_worth(stocks: Dict, date: str, lots: List) -> Numeric:
    worth = 0
    for lot in lots:
        stock_data = stocks[lot.stock]
        stock_worth = stock_data.at[date, "Close"]
        worth += stock_worth * lot.quanity
    return worth


class Portfolio:

    def __init__(self, long_cash: Numeric, short_cash: Numeric, stock_lots: List):
        self.long_cash = long_cash
        self.short_cash = short_cash
        self.stock_lots = stock_lots

    def append(self, lot):
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

        print("Cash: " + str(self.long_cash))

        print("---------------------------------")
