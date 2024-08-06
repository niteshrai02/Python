def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = list(map(sum, numbers, numbers, numbers))
print(result)

### Filter Function  ###
def fun(variable):
    letters = ['a', 'b', 'c', 'd']
    if(variable not in letters):
        return variable

lists = ['w', 'a', 's', 'b']
filtered = filter(fun, lists)
for i in range(len(lists)):
    print(fun(lists[i]))
