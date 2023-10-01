
from datetime import datetime

import stock.refactor.portfolio as srp
import stock.refactor.example.fake_data as fd


long_cash = 1000
short_cash = 1000
date = datetime.today().strftime('%Y%m%d')

portfolio_dict = srp.PortfolioWithDict(
    long_cash, short_cash, {'Long': fd.long_lots.copy(), 'Short': fd.short_lots.copy(), 'EMA': []}
)
portfolio_dict.stock_lots

portfolio_dict.add(fd.ema_lots[0])
portfolio_dict.stock_lots

portfolio_dict.remove(fd.ema_lots[0])
portfolio_dict.stock_lots

lw1 = portfolio_dict.get_long_worth(fd.stocks_lookup, date)
sw1 = portfolio_dict.get_short_worth(fd.stocks_lookup, date)

portfolio_dict.add(fd.long_lots[0])
portfolio_dict.stock_lots

lw2 = portfolio_dict.get_long_worth(fd.stocks_lookup, date)
lw2 == lw1

portfolio_list = srp.PortfolioWithList(long_cash, short_cash, fd.long_lots.copy() + fd.short_lots.copy())
portfolio_list.stock_lots
portfolio_list.get_long_worth(fd.stocks_lookup, date) == lw1
portfolio_list.get_short_worth(fd.stocks_lookup, date) == sw1

portfolio_set = srp.PortfolioWithSet(long_cash, short_cash, set(fd.long_lots + fd.short_lots))
portfolio_set.stock_lots

portfolio_set.get_long_worth(fd.stocks_lookup, date) == lw1
portfolio_set.add(fd.long_lots[0])
portfolio_set.stock_lots
portfolio_set.get_long_worth(fd.stocks_lookup, date) == lw1
portfolio_set.get_long_worth(fd.stocks_lookup, date) == lw2

portfolio_dict_deduped = srp.PortfolioWithDictDeduped(
    long_cash, short_cash, {'Long': fd.long_lots.copy(), 'Short': fd.short_lots.copy(), 'EMA': []}
)
portfolio_dict_deduped.get_long_worth(fd.stocks_lookup, date) == lw1

portfolio_dict_deduped.add(fd.long_lots[0])
portfolio_dict_deduped.stock_lots
portfolio_dict_deduped.get_long_worth(fd.stocks_lookup, date) == lw1
