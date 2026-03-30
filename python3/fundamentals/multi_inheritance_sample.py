class Person:
    def greet(self):
        print("Person greet.")


class Employee:
    def greet(self):
        print("Employee greet.")


class Manager(Employee, Person): #Python run greet method base on inheritance order (1.Employee 2.Person)
    pass

class ChifTechnologyOfficer(Person, Employee): #Python run greet method base on inheritance order (1.Person 2.Employee)
    pass

manager = Manager()
manager.greet()

cto = ChifTechnologyOfficer()
cto.greet()

