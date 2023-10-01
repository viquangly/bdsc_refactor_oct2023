
from stock.refactor.example.fake_data import generate_fake_stock_data
import stock.refactor.strategy as st
import stock.refactor.bull as bull
import stock.refactor.call as call

stock = generate_fake_stock_data('Costco')
stock_retriever = st.PriceRetriever(stock)

stock.iloc[-1]
stock_retriever.get_row(0)

stock.iloc[-2]
stock_retriever.get_price('High', -1)

stock_retriever[-1]
stock_retriever[-1].data

stock_retriever[0]
stock_retriever[0].data

stock_retriever[-2:].data

maru = bull.Marubozu()
maru.execute(stock_retriever)

lc = call.LongCall()
lc.calculate_cash(stock_retriever)
