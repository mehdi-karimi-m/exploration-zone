numberOfExpenses = int(input('Enter number of expenses:\n'))
expenses = []
for i in range(numberOfExpenses):
    expenses.append(float(input('Enter an expense:')))

total = sum(expenses)

print('You spend $', total, sep='')