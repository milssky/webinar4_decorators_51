def power_func_fabric(degree):
    def inner(number):
        return number**degree
    return inner


in_power_two = power_func_fabric(2)

print(type(in_power_two))
print(in_power_two(5))

in_power_five = power_func_fabric(5)  # inner -> return number**5

print(in_power_five(2))
