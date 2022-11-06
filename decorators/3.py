class Tracer:
    def __init__(self, func):
        self.calls = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Func {self._func.__name__} called {self.calls} nums")
        return self._func(*args, **kwargs)


# @Tracer
def foo():
    pass


foo = Tracer(foo)
foo()
foo()
foo()
foo()
