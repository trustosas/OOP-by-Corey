class Employee():
  
  raise_amount = 1.04
  emp_num = 0
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = f"{first.lower()}.{last.lower()}@company.com"
    Employee.emp_num+=1

  def full_name(self):
  	return f"{self.first} {self.last}"

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)
    #self.pay = int(self.pay * Employee.raise_amount)
    return self.pay
  
  #Class methods target attributes and methods(⁰00009) of a class and children that inherit from it
  @classmethod
  def set_raise_amount(cls, amt):
    cls.raise_amount = amt
    
  #Alternative constructor: offers another way to create instances
  @classmethod
  def from_string(cls, string):
    first, last, pay = string.split('-')
    return cls(first, last, pay)
  
  #Static methods do not take the instance (self) or the class (cls); they are just glorified functions with a logical relationship to the class
  @staticmethod
  def is_workday(day):
    if day.weekday() > 4:
      return False
    return True

#print(Employee.emp_num)

emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Osakpolor", "Osayande", 60000)

str_new_emp1 = "Jon-Snow-90000"

Employee.from_string(str_new_emp1)

#print(Employee.emp_num)

Employee.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp2.raise_amount)

import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))