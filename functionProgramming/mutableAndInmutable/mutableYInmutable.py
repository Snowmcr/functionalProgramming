scientists = [
    {"name": "Ada Lovelace", "field": "math", "born": 1815, "nobel": False},
    {"name": "Emmy Noether", "field": "math", "born": 1882, "nobel": False}
]
# This is not too good because is mutable.

import collections
Scientist = collections.namedtuple("Scientist", [
    "name", 
    "field", 
    "born", 
    "nobel",
])
ada = Scientist(name="Ada Lovelace", field="math", born=1815, nobel=False)
print(ada)
print(ada.name)
print(ada.field)
