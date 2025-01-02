from itertools import count, repeat, cycle

"""These are infinite iterators so we need to have some kind of logic to end the execution."""
def count_method(start: int, step: int) -> None:
    counter = count(start, step)

    for c in counter:
        print(c)

        if c == 100:
            break

def repeat_method(element: any, repetition: int) -> None:
    repeater = repeat(element, repetition)

    for r in repeater:
        print(r)

def cycle_method(element: str) -> None:
    cycler = cycle(element)

    i = 0
    for elem in cycler:
        if i < 10:
            print(elem)
            i += 1
        else:
            break


if __name__ == "__main__":
    count_method(10, 2)
    repeat_method("Hello", 3)
    cycle_method("ABCDE")