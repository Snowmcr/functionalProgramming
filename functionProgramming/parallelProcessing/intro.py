import collections
import time
from pprint import pprint

Scientist = collections.namedtuple("Scientist", [
    "name",
    "field",
    "born",
    "nobel",
])

scientists = (
    Scientist(name="Ada Lovelace", field="math", born=1815, nobel=False),
    Scientist(name="Emmy Noether", field="math", born=1882, nobel=False),
    Scientist(name="Marie Curie", field="physics", born=1867, nobel=True),
    Scientist(name="Tu Youyou", field="chemistry", born=1930, nobel=True),
    Scientist(name="Ada Yonath", field="chemistry", born=1939, nobel=True),
    Scientist(name="Vera Rubin", field="astronomy", born=1928, nobel=False),
    Scientist(name="Sally Ride", field="physics", born=1951, nobel=False)
)

pprint(scientists)
print()


def transform(x):
    print(f"Processing record {x.name}")
    time.sleep(3)
    result = {"name": x.name, "age": 2017 - x.born}
    print(f"Done processing record {x.name}")
    return result

result = tuple(map(
    transform,
    scientists
))

pprint(result)

"""
Right now, the program like it is, is gonna take a long time to end, because the map function is taking 
the iterables one after another secuencially, so one and then another.
The thing is, it can be better with multiprocessing.
"""