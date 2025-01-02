from itertools import accumulate, chain, compress, pairwise
from typing import List

def accumulate_method(elements: List) -> None:
    sum = accumulate(elements)
    print(list(sum))

def chain_method(elements1: str, elements2: str) -> None:
    chained = chain(elements1, elements2)
    print(list(chained))

def chain_from_iterable(iterable: List) -> None:
    chained = chain.from_iterable(iterable)
    print(list(chained))

def compress_method(data: List, selectors: List) -> None:
    compressed = compress(data, selectors)
    print(list(compressed))

def pairwise_method(iterable: List) -> None:
    paired = pairwise(iterable)
    print(list(paired))

if __name__ == "__main__":
    accumulate_method([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    chain_method("ABC", "DEF") # ['A', 'B', 'C', 'D', 'E', 'F']
    chain_from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    compress_method([[1, 2, 3], ["A", "B", "C"], [False, False, True]], [True, True, False]) # [[1, 2, 3], ['A', 'B', 'C']]
    pairwise_method(["A", "B", "C", "D", "E", "F", "G"]) # [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')]