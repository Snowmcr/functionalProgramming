import collections
from pprint import pprint
from functools import reduce
import itertools

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

scintists_by_field = {
    item[0]: list(item[1])
    for item in itertools.groupby(scientists, lambda x: x.field)
}
print()
# pprint(scintists_by_field)
