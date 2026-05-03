#1. Classes are blueprints for creating Class instances
class Employee():
  
  #2. The init method enables quick "init-ialization" of Instance Attributes from the instance creation, passed as parameters; "self" is used to refer to the Class itself, and is always passed as the first parameter to each method in definition.
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = f"{first.lower()}.{last.lower()}@company.com"
  
  #3. A class method is simply a function of a class.
  def full_name(self):
  	return f"{self.first} {self.last}"
  	
#4. Creation of Class instances
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Osakpolor", "Osayande", 60000)

#5. Retrieving instance attributes
print(emp1.email)
print(emp2.email)

#6. Using instance methods
print(emp1.full_name())

#7. Another syntax for using instance methods 
print(Employee.full_name(emp2))