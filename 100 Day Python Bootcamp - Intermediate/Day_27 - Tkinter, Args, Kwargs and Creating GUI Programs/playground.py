# *Args: Many Positional Arguments

def add(*args):

    print(args[1]) # Getting the arg with specified position

    for n in args:
       n = sum(args)
    return n

print(add(3, 5, 6))

# **Kwargs: Optional Keyword Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.make)

