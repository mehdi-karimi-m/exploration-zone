name = input("What's your name?\n")
income = int(input("How much you get?\n"))
tax = float(input("What is the Tax amount?\n"))
salary = income - income*tax
print("Dear " + name + "your salary is: " + str(salary))