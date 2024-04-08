# map
from functools import reduce

tab = [1, 2, 3, 5]


def pow(x):
    return x ** 2


tab2 = list(map(pow, tab))

tab3 = list(map(lambda x: x ** 2, tab))
print(tab2)
print(tab3)

# reduce
tab = [1, 2, 3, 4, 5, 6]
tab3 = reduce(lambda x, y: x + y, tab)
print(tab3)
# filter
tab4 = list(filter(lambda x: x % 3 == 0 and x % 2 == 0, tab))
print(tab4)

# zip
tab = [1, 2, 3]
tab1 = [1, 2, 3]
print(tuple(zip(tab, tab1)))
keys = ["jogurt", "jabłko", "masło"]
values = [1, 2, 3, 4]
print(dict(zip(keys, values)))

import operator
## Math operations: add(), sub(), mul(), floordiv(), abs()
## Logical operations: not_(), truth()
## Bitwise operations: and_(), or_(), invert()
## Comparisons: eq() -> equal to, ne() -> not equal, lt()->less than,
## le()-less or equal, gt() -> greater than, and ge() -> greater or equal
## Object identity: is_(), is_not()

import functools, operator

list2 = [2, 2, 3, 4]
resultReduce2 = functools.reduce(operator.mul, list2, 2)
print(resultReduce2)
lista = [1, 2, 3]
for i, j in enumerate(lista):
    print(i, j)

dict2 = {'fds': 1, 'fdsf': 4}
print(dict2.items())
