my_stack = []
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)

print(my_stack)
item = my_stack.pop()
print(item)
print(my_stack)
if not my_stack:
    print(my_stack[-1])

item = my_stack.pop()
print(item)
item = my_stack.pop()
print(item)

my_stack.pop()