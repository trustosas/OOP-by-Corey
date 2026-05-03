class Employee():
  
  #1. Class attributes are variables availiable to a class and all it's instances.
  raise_amount = 1.04
  emp_num = 0
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = f"{first.lower()}.{last.lower()}@company.com"
    #3. Here we use Class_Name because we want to globalize to get the number of all employees
    Employee.emp_num+=1

  def full_name(self):
  	return f"{self.first} {self.last}"

  def apply_raise(self):
    
    #2. Within a Class, attributes can be referred to with "self" which makes it referrence the value for that instance, or the Class_Name, which makes it referrence the value for the Class itself. Using "self" is more flexible and recommended when you need to localize the attributes, if not, use Class_Name.
    self.pay = int(self.pay * self.raise_amount)
    #self.pay = int(self.pay * Employee.raise_amount)
    return self.pay

#4. Before instantiating 2 employees
print(Employee.emp_num)

emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Osakpolor", "Osayande", 60000)

#5. After instantiating 2 employess
print(Employee.emp_num)