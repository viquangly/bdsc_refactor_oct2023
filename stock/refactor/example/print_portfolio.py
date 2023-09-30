
def print_portfolio(stock_lot_dict):
    print("---------------------------------")
    for stock_lot in stock_lot_dict:
        for lot in stock_lot:
            print(lot)

    print("---------------------------------")


stock_lot_dict = {
    'Long': [],
    'Short': [],
    'EMA': []
}

print_portfolio(stock_lot_dict)

long_cash = 123456.789
print(f'Cash: ${long_cash:,.2f}')
