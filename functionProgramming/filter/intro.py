import collections
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

a = tuple(filter(lambda x: x.nobel is True, scientists))
pprint(a)

# pprint(tuple(filter(..., scientists)))
# with the ... including a function, it owuld change the filter.