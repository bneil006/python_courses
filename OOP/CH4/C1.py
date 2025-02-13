class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.length + self.width)


# This one felt a little strange, using the super().__init__(length, length) when in the above parent i had length and width variables
# I can see why and how this works but it feels strange none the less
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


def main():
    list_of_items = [Square(5), Square(3), Square(10), Rectangle(5, 10), Rectangle(10, 2)]

    for item in list_of_items:
        print(f"AREA: {item.get_area()}, PERIMETER: {item.get_perimeter()}")


main()