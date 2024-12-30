class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_values(self):
        print(f"x: {self.x}, y: {self.y}")

if __name__ == "__main__":
    rect = Rectangle(3, 5)
    rect.print_values()

    str1 = "Hello"
    str2 = " World!"

    print(str1 + str2)
    # + = __add__()
    print(str1.__add__(str2))

    print(len(str1))
    # len() = __len__()
    print(str1.__len__())