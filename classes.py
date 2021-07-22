# Classes
class Employee:

    num_of_emps = 0
    raise_ammount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapany.com'
        # increase the emp by adding a new member
        Employee.num_of_emps += 1

    def fullname(self): # fullname
        return '{} {}'.format(self.first, self.last)
    # have to call this with parenthesis EX:-"Employee.fullname()"
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last,
                self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def apply_raise(self): # raising payment
        self.pay = int(self.pay * self.raise_ammount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_ammount = amount

# inheritance
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    
emp_1 = Developer('murali', 'krishna', 6000, 'javaScript')
emp_2 = Developer('sona', 'gorty', 5000, 'java')

mgr_1 = Manager('rohith', 'bathini', 4000, [emp_1])

print(emp_1)
print(mgr_1.print_emps())
mgr_1.add_emp(emp_2)
print(mgr_1.print_emps())
mgr_1.remove_emp(emp_1)
print(mgr_1.print_emps())
#repr(emp_1)
#str(emp_1)
