for i in range(5):
    print(i)

for j in range(0, 10, 9):
    print(j)

for i in range(len([1, 2, 3])):
    print(i)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        return area
    
circle_instance = Circle(5)

print(circle_instance.calculate_area())