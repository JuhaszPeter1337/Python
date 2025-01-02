r = range(1, 10)

i = iter(r)

print(list(i))

j = iter(r)

for k in j:
    print(k)

"""
1. range(1, 5): iterable object
2. it is going to call the iter() function on the iterable object
3. it return with an iterator
4. the for loop is going to continually call the next() method on this iterator until the exception raised
"""
for number in range(1, 5):
    print(number)