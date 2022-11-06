class Test:
    def __call__(self, *args, **kwargs):
        print(f"Called {self.__class__.__name__}")


t = Test()
print(type(t))
t()
