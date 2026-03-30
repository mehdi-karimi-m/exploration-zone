#You can use sharp to write comments in python

findOddNumbersBefore = int(input('Find odd numbers before (maximum is 100):\n')) # 35
count = 0;
for n in range(findOddNumbersBefore):
    if n > 100: break
    if n % 2 != 0: 
        print(n, 'is odd number.')
        count = count + 1

print('There is', end=' ')
print(count, end=' ')
print('odd numbers')
