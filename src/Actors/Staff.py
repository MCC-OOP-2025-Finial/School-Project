import Actor_Main as ActorMain
import random

class Staff(ActorMain.ActorMain):
    def __init__(self, role, salary, hoursWorkedWeek, experienceYears):
        super().__init__()
        self.role = role
        self.experienceYears = random.randint(0,35)
        self.salary = self.calculateSalary()

    def calculateSalary(self):
        if self.role == "Teacher":
            return 
        elif self.role == "Princaple":
            return "104,000"
        elif self.role == "Vice Principle":
            return "86,000"
        elif self.role == "Custodian":
            return "30,000"
        elif self.role == "Resource Officer":
            return "79,000"
        elif self.role == "Coach":
            return "43,000"
        elif self.role == "IT":
            return "54,000"
        elif self.role == "Nurse":
            return "67,000"
        elif self.role == "Guidance Counsler":
            return "60,000"

class teacher(Staff):
    salary = "63,000"
    def getSalary(self):
        return self.SALARY
    pass
class principle(Staff):
    salary = "104,000"
    def getSalary(self):
        return self.salary
    pass
class vicePrinciple(Staff):
    salary = "86,000"
    def getSalary(self):
        return self.salary
    pass
class custodian(Staff):
    salary = "30,000"
    def getSalary(self):
        return self.salary
    pass
class resourceOfficer(Staff):
    salary = "79,000"
    def getSalary(self):
        return self.salary
    pass
class coach(Staff):
    salary = "43,000"
    def getSalary(self):
        return self.salary
    pass
class it(Staff):
    salary = "54,000"
    def getSalary(self):
        return self.salary
    pass
class nurse(Staff):
    salary = "67,000"
    def getSalary(self):
        return self.salary
    pass
class guidanceCounsler(Staff):
    salary = "60,000"
    def getSalary(self):
        return self.salary
    pass

def createStaffRoles(role, salary, hoursWorkedWeek, experienceYears):
    mapping = {
        "Teacher": teacher,
        "Princaple": principle,
        "Vice Principle": vicePrinciple,
        "Custodian": custodian,
        "Resource Officer": resourceOfficer,
        "Coach": coach,
        "IT": it,
        "Nurse": nurse,
        "Guidance Counsler": guidanceCounsler,
    }

    return mapping[role](role, salary, hoursWorkedWeek, experienceYears)
