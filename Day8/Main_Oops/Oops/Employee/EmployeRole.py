from EmpCompany import Employe
class EmpCompany(Employe):
    def __init__(self,name):
        self.name=name
    def FullStackrole(self):
        return f"{self.name} Full-Stack Dev"
    def FrontEndrole(self):
        return f"{self.name} Full-Stack Dev"
emp1=EmpCompany("Sankar")
print(emp1.FullStackrole())
emp2=EmpCompany("Murali")
print(emp2.FrontEndrole())