# This class provides basic implementations for the .__iter__() method.
from collections.abc import Iterator
from typing import Any

#.__iter__(): Called to initialize the iterator. It must return an iterator object.
#.__next__(): Called to iterate over the iterator. It must return the next value in the data stream.

# Creating iterator and looping through
'''
if __name__ == "__main__":
    my_list = [1, 4, 7]

    my_iterator = iter(my_list)
    
    print(my_iterator)
    print(my_iterator.__next__())
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
'''

# Creating iterator class from scratch
'''
class SequenceIterator:
    def __init__(self, sequence) -> None:
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
if __name__ == "__main__":
    my_iter = SequenceIterator(my_list)
    next(my_iter)
    print(next(my_iter))

    for iter in SequenceIterator([1, 2, 3, 4]):
        print(iter)
'''

# Creating Square iterator
'''
class SquareIterator:
    def __init__(self, sequence) -> None:
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self._index < len(self._sequence):
            square = self._sequence[self._index] ** 2
            self._index += 1
            return square
        else:
            raise StopIteration
        
if __name__ == "__main__":
    for square in SquareIterator([1, 2, 3, 4, 5]):
        print(square)
'''

# Creating Fibonacci iterator
'''
class FibonacciIterator:
    def __init__(self, stop = 10) -> None:
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        if self._index < self._stop:
            fib_number = self._current
            #self._current = self._next
            #self._next = fib_number + self._next
            self._current, self._next = (self._next, self._current + self._next)
            self._index += 1 
            return fib_number
        else:
            raise StopIteration
        
if __name__ == "__main__":
    for fib in FibonacciIterator():
        print(fib)
'''

# Creating infinite Fibonacci iterator
'''
class InfiniteFibonacciIterator:
    def __init__(self) -> None:
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self
    
    def __next__(self) -> Any:
        fib_number = self._current
        self._current, self._next = (
            self._next,
            self._current + self._next
        )
        self._index += 1
        return fib_number
    
if __name__ == "__main__":
    for fib in InfiniteFibonacciIterator():
        print(fib)
'''

# Inheriting from collections.abc.Iterator
'''
class SequenceIterator(Iterator):
    def __init__(self, sequence) -> None:
        self._sequence = sequence
        self._index = 0

    def __next__(self) -> Any:
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

if __name__ == "__main__":
    for iter in SequenceIterator([1, 2, 3, 4]):
        print(iter)
'''

'''
Generator functions are special types of functions that allow you to create iterators using a functional style. Unlike regular functions,
which typically compute a value and return it to the caller, generator functions return a generator iterator that yields a stream of data one value at a time.
In Python, you'll commonly use the term generators to collectively refer to two separate concepts: the generator function and the generator iterator.
The generator function is the function that you define using the yield statement. The generator iterator is what this function returns.
A generator function returns an iterator that supports the iterator protocol out of the box.
To create a generator function, you must use the yield keyword to yield the values one by one.
'''

# Creating Generator Functions
'''
def sequence_generator(sequence):
    for item in sequence:
        yield item

if __name__ == "__main__":
    for number in sequence_generator([1, 2, 3, 4]):
        print(number)
'''

# Using Generator Expressions to Create Iterators
'''
[item for item in [1, 2, 3, 4]] # List comprehension

(item for item in [1, 2, 3, 4]) # Generator expression

if __name__ == "__main__":
    list_comprehension = [item for item in [1, 2, 3, 4]]
    for number in list_comprehension:
        print(number)

    generator_expression = (item for item in [1, 2, 3, 4])
    for number in generator_expression:
        print(number)
'''

# Exploring Different Types of Generator Iterators
'''
def square_generator(sequence):
    for item in sequence:
        yield item ** 2

def fibonacci_generator(stop = 10):
    current_value, next_value = 0, 1
    for _ in range(0, stop):
        fib_number = current_value
        current_value, next_value = (
            next_value,
            current_value + next_value
        )
        yield fib_number

if __name__ == "__main__":
    print("Square numbers:")
    for number in square_generator([1, 2, 3, 4, 5]):
        print(number)

    print("Fibonacci numbers:")
    for number in fibonacci_generator():
        print(number)

    fibonacci_series = [number for number in fibonacci_generator(30)]
    print(fibonacci_series)
'''