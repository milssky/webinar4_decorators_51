from functools import wraps


def hello_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} decorated")
        return func(*args, **kwargs)
    return wrapper


@hello_decorator
def foo():
    pass


print(foo.__name__)  # foo

