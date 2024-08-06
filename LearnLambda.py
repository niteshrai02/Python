import functools

str1 = "geeksforgeeks"
upper = lambda string: string.upper()
print(upper(str1))

Max = lambda a, b: a if a > b else b
print(Max(1,2))

ages = [16, 25, 80, 12]
adults = list(filter(lambda age: age > 18, ages))
print(adults)