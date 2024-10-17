add_1 = lambda x: x + 1
add_two_int = lambda x, y: x + y

result1 = add_1(2)
result2 = add_two_int(2,3)

print(result1)
print(result2)

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print(squares)

filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)

values = [(1, 'b', "hello"), (2, 'a', "world"), (3, 'c', "!")]

sorted_values = list(sorted(values, key=lambda x: x[1]))
print(sorted_values)