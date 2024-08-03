varList = []
print("Empty List", varList)
varList = ["Nitesh", 1, True]
print("values", varList[0])

b = varList[0]+ str(varList[1])
print(b)
a = (list(varList[0]))
print(a)
string = "".join(reversed("Hellow"))
print(string)
print(len(varList))
reversList = [1, 2, 3, 4, 5]

print(reversList)
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x**2)

print(odd_square)