a = 10
b = 5
if a > b or b > 0:
    print("a is greater than b")
else:
    print("b is greater than a")

def runMatch():
    num = int(input("Enter a number between 1 and 3: "))

    match num:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            print(3)
        case _:
            print("no MAtch")

runMatch()
    
