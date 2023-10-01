
from stock.refactor.example.fake_data import long_lots, short_lots, ema_lots

long_lots[0].get_stock_tag()
long_lots[1].get_stock_tag()
long_lots[2].get_stock_tag()

short_lots[0].get_stock_tag()
short_lots[1].get_stock_tag()
short_lots[2].get_stock_tag()

ema_lots[0].get_stock_tag()
ema_lots[1].get_stock_tag()
ema_lots[2].get_stock_tag()

ema_lots[2].get_unique_id()
print(ema_lots[2])
