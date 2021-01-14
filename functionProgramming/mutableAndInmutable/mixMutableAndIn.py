import collections
from pprint import pprint
Scientist = collections.namedtuple("Scientist", [
    "name", 
    "field", 
    "born", 
    "nobel",
])

scientists = [
    Scientist(name="Ada Lovelace", field="math", born=1815, nobel=False),
    Scientist(name="Emmy Noether", field="math", born=1882, nobel=False)
]
pprint(scientists)
del scientists[0]
# The problem is that a list is mutable, and wea re mixing them.
