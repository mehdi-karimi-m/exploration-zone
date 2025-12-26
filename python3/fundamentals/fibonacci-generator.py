fiboNum = int(input("Enter a number: "))

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(fiboNum):
    print(next(gen))