expenses = [20.5, 12.78, 58, 33.01, 8, 10, 20]
sumOfExpenses = 0
print('expenses list:')
for expense in expenses:
    sumOfExpenses = sumOfExpenses + expense
    print(expense)

print('Sum of expenses is:', sumOfExpenses)
print('--------------------------')
total = sum(expenses)
print('You spent $', total, sep='')