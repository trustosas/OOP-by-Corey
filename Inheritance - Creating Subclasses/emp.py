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
    return self.pay
  
  @classmethod
  def set_raise_amount(cls, amt):
    cls.raise_amount = amt
    
  @classmethod
  def from_string(cls, string):
    first, last, pay = string.split('-')
    return cls(first, last, pay)
  
  @staticmethod
  def is_workday(day):
    if day.weekday() > 4:
      return False
    return True
    
class Developer(Employee):
  raise_amount = 1.10
  
  #__init__ can be extended with super(), like so:
  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    self.prog_lang = prog_lang

class Manager(Employee):
  
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    #Corey's advice: You never want mutables as default arguments in your code
    if employees is not None:
      self.employees = employees
    else:
      self.employees = []
      
  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)
  
  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
      
  def print_emps(self):
    for emp in self.employees:
      print("-->", emp.full_name())

dev1 = Developer("Corey", "Schafer", 50000, 'Python')
dev2 = Developer("Osakpolor", "Osayande", 60000, 'JavaScript')

mgr1 = Manager('Sue', 'Azul', 10000, [dev1])

#print(dev1.prog_lang)
#print(dev1.email)

#Print employee
#print(mgr1.email)
#mgr1.print_emps()
#print()

#Add new employee
#mgr1.add_emp(dev2)
#mgr1.print_emps()
#print()

#Remove employee
#mgr1.remove_emp(dev1)
#mgr1.print_emps()

#Useful for testing inheritance
#print(isinstance(dev1, Employee))
#print(issubclass(Manager, Employee))