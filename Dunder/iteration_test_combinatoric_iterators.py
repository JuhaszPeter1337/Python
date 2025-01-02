from itertools import product, permutations, combinations
from typing import List

def product_method(iterable1: List, iterable2: List) -> None:
    result = product(iterable1, iterable2)
    print(list(result))

# Factorial
def permutations_method(iterable: List | str, size: int) -> None:
    perm = permutations(iterable, size)
    print(list(perm))

def combinations_method(iterable: List | str, size: int) -> None:
    comb = combinations(iterable, size)
    print(list(comb))

if __name__ == "__main__":
    product_method(["A", "B", "C"], [1, 2, 3]) # [('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3), ('C', 1), ('C', 2), ('C', 3)]
    permutations_method(["A", "B", "C", "D"], 2) # [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
    permutations_method("ABCD", 2) # [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
    combinations_method("ABCD", 2) # [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]