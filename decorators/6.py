from functools import wraps


def decorator_with_args(input_arg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'arguments of decorator {input_arg}')
            result = func(*args, **kwargs)
            return f'{input_arg}\n{result}\n{input_arg}'
        return wrapper
    return decorator


@decorator_with_args("------------")
def foo(a, b, c):
    return a + b + c


# result = foo(1, 2, 4)

# print(result)

print(foo.__name__)
