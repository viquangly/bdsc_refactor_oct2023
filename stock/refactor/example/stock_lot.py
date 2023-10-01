
from stock.refactor.example.fake_data import long_lots, short_lots, ema_lots

long_lots[0].tag
long_lots[1].tag
long_lots[2].tag

short_lots[0].tag
short_lots[1].tag
short_lots[2].tag

ema_lots[0].tag
ema_lots[1].tag
ema_lots[2].tag

ema_lots[2].get_unique_id()
print(ema_lots[2])
