
class Foo:

    tag = 1

    def __init__(self):
        Foo.tag += 1


class Bar(Foo):
    ...


foo = Foo()
foo.tag

tango = Foo()
tango.tag

foo.tag

bar = Bar()
bar.tag

foo.tag
