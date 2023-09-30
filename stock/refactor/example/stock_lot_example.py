
import itertools

tag_counter = itertools.count()


class FakeStockLotLong:

    def __init__(self):
        self.tag = next(tag_counter)

    def get_stock_tag(self):
        return self.tag

    def get_unique_tag_option2(self):
        return id(self)


class FakeStockLotShort:

    def __init__(self):
        self.tag = next(tag_counter)

    def get_stock_tag(self):
        return self.tag

    def get_unique_tag_option2(self):
        return id(self)


class FakeStockLotEMA:

    def __init__(self):
        self.tag = next(tag_counter)

    def get_stock_tag(self):
        return self.tag

    def get_unique_tag_option2(self):
        return id(self)


long0, long1, long2 = (FakeStockLotLong() for x in range(3))
short0, short1, short2 = (FakeStockLotShort() for x in range(3))
ema0, ema1, ema2 = (FakeStockLotEMA() for x in range(3))

long0.get_stock_tag()
long1.get_stock_tag()
long2.get_stock_tag()

short0.get_stock_tag()
short1.get_stock_tag()
short2.get_stock_tag()

ema0.get_stock_tag()
ema1.get_stock_tag()
ema2.get_stock_tag()

ema2.get_unique_tag_option2()
