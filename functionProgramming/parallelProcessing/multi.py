
import collections
import time
import multiprocessing
import os
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


def transform(x):
    print(f"Process {os.getpid()} working record {x.name}")
    time.sleep(3)
    result = {"name": x.name, "age": 2017 - x.born}
    print(f"Process {os.getpid()} done processing record {x.name}")
    return result


""" 
start = time.time()

pool = multiprocessing.Pool()
result = pool.map(transform, scientists)

# result = tuple(map(
#     transform,
#     scientists
# ))

end = time.time()

print(f"time to complete: {end-start:.2f}")
pprint(result)
"""

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:  # processes=len(scientists)
        start = time.time()
        result = pool.map(transform, scientists)
        end = time.time()
        print(f"Time taken: {end - start:.2f}")
        pprint(result)

# Not too hard to change to multiprocessing prgramming while doing functional.
