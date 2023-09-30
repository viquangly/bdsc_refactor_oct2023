
from stock.refactor.example.fake_stock import stock
import stock.refactor.strategy as st
import stock.refactor.bull as bull
import stock.refactor.call as call

stock_index = st.PriceRetriever(stock)

stock.iloc[-1]
stock_index.get_row(0)

stock.iloc[-2]
stock_index.get_price('High', -1)

stock_index[-1]
stock_index[-1].data

stock_index[0]
stock_index[0].data

stock_index[-2:].data

maru = bull.Marubozu()
maru.execute(stock_index)

lc = call.LongCall()
lc.calculate_cash(stock_index)
