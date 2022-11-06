# Нам нужно написать декоратор, который бы в консоль печатал название вызываемой функции
# Вызвана функция с именем: ...
# результаты функции

def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция с именем {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def foo(param1, **kwargs):
    print("Я функция foo", param1)
    print("kwargs:")
    for key, value in kwargs.items():
        print(key, value)
    return 100

foo(500)
print("*********************")
d = {'b': 10000, 'c': 5000}  # d.items() -> [('b', 10000), ('c', 5000)]
foo = print_decorator(foo)
a = foo(500, **d)  # foo(500, b=10000, c=5000)
print(a)

# b = [1, 2, 3, 100]
# print(*b)
# d = {'b': 10000, 'c': 5000}
#
# def f(*args, **kwargs):
#     for item, value in kwargs.items():
#         print(item, value)
#

# f(10, 20, 30, 40, ...)


@print_decorator
def bar():
    pass


bar = print_decorator(bar)

