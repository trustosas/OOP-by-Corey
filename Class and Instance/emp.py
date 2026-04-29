class Employee():
 def __init__(self, first, last, pay):
  self.first = first
  self.last = last
  self.pay = pay
  self.email = f"{first.lower()}.{last.lower()}@company.com"

emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Osakpolor", "Osayande", 60000)

print(emp2.email)