class EmptyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        print(f"{self.func.__name__} decorated!")


class Foo:
    @EmptyDecorator
    def bar_method(self, x, y):
        print(x + y)


foo_obj = Foo()
foo_obj.bar_method(1, 2)

