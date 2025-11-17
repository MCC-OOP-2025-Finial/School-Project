import Actor_Main as ActorMain
import random

class Staff(ActorMain.ActorMain):
    def __init__(self, role, salary, hoursWorkedWeek, experienceYears):
        super().__init__()
        self.role = role
        self.experienceYears = random.randint(0,35)
        
# Subclasses for staff roles
class teacher(Staff):
    def __init__(self,homeroom)
        self.homeroom = classroom
    salary = "63,000"
    def teach():
        pass
    def prepareLesson():
        pass
    def recordAttendance():
        pass
    def getSalary(self):
        return self.salary
        
class principle(Staff):
    salary = "104,000"
    def sendAnnouncement():
    announcement = input("Enter announcement: ")
    return f"Announcement: {announcement}"
    def evaluateTeacher()
        pass
    def getSalary(self):
        return self.salary
        
class vicePrinciple(Staff):
    salary = "86,000"
    def getSalary(self):
        return self.salary
        
class custodian(Staff):
    def cleanRoom():
        location = self.location
        return f"{location} was cleaned."
    def resupplyRoom()
        location = self.location
        return f"{location} was resupplied."
    salary = "30,000"
    def getSalary(self):
        return self.salary
        
class resourceOfficer(Staff):
    salary = "79,000"
    def getSalary(self):
        return self.salary
    def apprehend(location, name):
        return f"{name} has been apprehended."
    def search(location, name):
        return f"{name} has been searched."
        
class coach(Staff):
    salary = "43,000"
    def getSalary(self):
        return self.salary
        
class it(Staff):
    salary = "54,000"
    def getSalary(self):
        return self.salary
    def fixComputer()
        pass
        
class nurse(Staff):
    salary = "67,000"
    def getSalary(self):
        return self.salary
    def checkHealth()
        pass
    def tendTo
        pass
        
class guidanceCounsler(Staff):
    salary = "60,000"
    def getSalary(self):
        return self.salary
    def counsel():
        pass

class secratary(Staff):
    salary = "55,000"
    def getSalary(self):
        return self.salary
    def greet()
        pass
    def doClericalDuty()
        pass

class cafetieriaWorker(Staff)
    salary = "30,000"
    def getSalary(self)
        return self.salary
    def serveFood()
        pass
    def cleanCafetieria()
        pass
    def assistStudent()
        pass
        
# Creates the roles
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
        "Cafetieria Worker": cafetieriaWorker,
        "Secratary": secratary,
    }

    return mapping[role](role, salary, hoursWorkedWeek, experienceYears)
