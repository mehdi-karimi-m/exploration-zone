from sys import getsizeof

values = [x * 2 for x in range(10)]
print("list:", getsizeof(values))
print(type(values))
print(values)

values = (x * 2 for x in range(10))
print("gen:", getsizeof(values))
print(type(values))
print(values)
