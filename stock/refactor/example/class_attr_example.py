
class Foo:

    tag = 1

    def __init__(self):
        Foo.tag += 1

    def get_stock_tag(self):
        return Foo.tag


class Bar(Foo):
    ...


foo = Foo()
foo.get_stock_tag()

tango = Foo()
tango.get_stock_tag()

foo.get_stock_tag()

bar = Bar()
bar.get_stock_tag()
foo.get_stock_tag()
