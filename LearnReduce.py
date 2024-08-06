import functools
import operator
import itertools

list1 = [1, 2, 3, 5.5, 5]

print(functools.reduce(lambda a, b: a + b, list1))
print(functools.reduce(lambda a, b: a if a > b else b, list1))

print(functools.reduce(operator.add, list1))
print(functools.reduce(operator.mul, list1))

print(list(itertools.accumulate(list1, lambda x, y: x + y)))