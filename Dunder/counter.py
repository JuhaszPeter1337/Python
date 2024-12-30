class Counter():
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value -= 1

    def __str__(self):
        return f"Counter value: {self.value}"
    
    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        elif isinstance(other, int):
            return self.value + other
        else:
            raise TypeError("Invalid type of object!")

if __name__ == "__main__":
    counter1 = Counter()
    counter2 = Counter()

    counter1.count_up()
    counter2.count_down()

    print(counter1.value, counter2.value)
    print(counter1.value + counter2.value)
    print(str(counter1))
    print(counter1 + counter2)
    print(counter1 + 5)
    print(counter1 + "5")