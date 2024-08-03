import array as arr


a = arr.array('i', [1,2,3])
for i in range(0, 3):
    print(a[i])
print(a*70)

Dict = {1: "test", 2: "hello", 3: [1,2,3], 4: ""}
print(Dict[3])

set1 = set([1,2,2,3,4,4])
print(set1)

set2 = set()
set2.add(1)
set2.add(3)
for i in range(1,6):
    set2.add(i)
    print(set2)
    
# Type casting
var1 = 4.0
x = int(var1)
print(type(x))
print(x)

string1 = "t"
int1 = 10
final = str(int1) + string1
print(final)