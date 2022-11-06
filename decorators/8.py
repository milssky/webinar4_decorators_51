def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция с именем {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def other_print_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Это другой декоратор")
        return func(*args, **kwargs)
    return wrapper


@print_decorator
@other_print_decorator
def foo():
    print("Вызвана Foo")


foo = other_print_decorator(foo)
foo = print_decorator(foo)


