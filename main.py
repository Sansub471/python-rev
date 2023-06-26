# Python object-oriented Programming

#class Employee:
    #pass

# emp1 = Employee()
# emp2 = Employee()


# emp1.name='Subash'
# emp2.name='Udaya'
# This is also a way of instantiating attributes.

#print(emp1.name)
#print(emp2.name)

# Now lets create a class so that we can model Employee better

from distutils.command.build_scripts import first_line_re


class Employee:
    
    # This is like a constructor
    # It will run automatically when an instance is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # self is the automatic argument, like 'this*' pointer in C++
    def fullname(self):
        fname = self.first + ' ' + self.last
        return fname

emp1 = Employee('Subash', 'Mainali', 100000)
emp2 = Employee('Santosh', 'Mainali', 50000)

print(emp1.fullname())

#11 emp1.fullname()
#22 Employee.fullname(emp1)
# 11 and 22 are basically the same statements