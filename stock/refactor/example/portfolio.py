
from copy import deepcopy
from datetime import datetime
import itertools
from typing import Dict, Collection

from stock.refactor.stock_lot import StockLot
import stock.refactor.portfolio as srp
from stock.refactor.example.stock_lot import long_lots, short_lots, ema_lots
from stock.refactor.example.fake_stock import generate_fake_stock_data


def create_stocks_lookup(lots: Collection[StockLot]) -> Dict:
    return {lot.stock: generate_fake_stock_data(lot.stock) for lot in lots}


all_lots = list(itertools.chain(long_lots, short_lots, ema_lots))
stocks_lookup = create_stocks_lookup(all_lots)
long_cash = 1000
short_cash = 1000
date = datetime.today().strftime('%Y%m%d')

portfolio_dict = srp.PortfolioWithDict(
    long_cash, short_cash, {'Long': deepcopy(long_lots), 'Short': deepcopy(short_lots), 'EMA': []}
)
portfolio_dict.stock_lots

portfolio_dict.add(ema_lots[0])
portfolio_dict.stock_lots

portfolio_dict.remove(ema_lots[0])
portfolio_dict.stock_lots

lw1 = portfolio_dict.get_long_worth(stocks_lookup, date)
sw1 = portfolio_dict.get_short_worth(stocks_lookup, date)

portfolio_dict.add(long_lots[0])
portfolio_dict.stock_lots

lw2 = portfolio_dict.get_long_worth(stocks_lookup, date)
lw2 == lw1

portfolio_list = srp.PortfolioWithList(long_cash, short_cash, long_lots + short_lots)
portfolio_list.stock_lots
portfolio_list.get_long_worth(stocks_lookup, date) == lw1
portfolio_list.get_short_worth(stocks_lookup, date) == sw1

portfolio_set = srp.PortfolioWithSet(long_cash, short_cash, set(long_lots + short_lots))
portfolio_set.stock_lots

portfolio_set.get_long_worth(stocks_lookup, date) == lw1
portfolio_set.add(long_lots[0])
portfolio_set.stock_lots
portfolio_set.get_long_worth(stocks_lookup, date) == lw1
portfolio_set.get_long_worth(stocks_lookup, date) == lw2
