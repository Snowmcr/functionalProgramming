import collections
import functools

Car = functools.namedtuple("Car", [
    "color",
    "year",
    "model"
])

my_car = Car(color="blue", year=2021, model="Performante")

print(my_car.color)
