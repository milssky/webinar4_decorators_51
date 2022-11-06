x = 10


def foo():
    global x
    x = 100


foo()
print(x)

