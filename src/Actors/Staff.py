import Actor_Main as ActorMain
import random

class Staff(ActorMain.ActorMain):
    def __init__(self, role, salary, hoursWorkedWeek, experienceYears):
        super().__init__()
        self.role = role
        self.salary = salary
        self.hoursWorkedWeek = hoursWorkedWeek
        self.experienceYears = experienceYears

# Role subclasses
class teacher(Staff):
    def __init__(self, role, salary, hoursWorkedWeek, experienceYears, homeroom):
        super().__init__(role, salary, hoursWorkedWeek, experienceYears)
        self.homeroom = homeroom
    salary = "63,000"
    def teach(self):
        pass
    def prepareLesson(self):
        pass
    def recordAttendance(self):
        pass
    def getSalary(self):
        return self.salary

class principal(Staff):
    salary = "104,000"
    def sendAnnouncement(self):
        announcement = input("Enter announcement: ")
        return f"Announcement: {announcement}"
    def evaluateTeacher(self):
        return f"Teacher has been evaluated."
    def getSalary(self):
        return self.salary

class vicePrincipal(Staff):
    salary = "86,000"
    def getSalary(self):
        return self.salary

class custodian(Staff):
    salary = "30,000"
    def cleanRoom(self):
        return f"{self.location} was cleaned."
    def resupplyRoom(self):
        return f"{self.location} was resupplied."
    def getSalary(self):
        return self.salary

class resourceOfficer(Staff):
    salary = "79,000"
    def getSalary(self):
        return self.salary
    def apprehend(self, location, name):
        return f"{name} has been apprehended."
    def search(self, location, name):
        return f"{name} has been searched."

class coach(Staff):
    salary = "43,000"
    def getSalary(self):
        return self.salary

class it(Staff):
    salary = "54,000"
    def getSalary(self):
        return self.salary
    def fixComputer(self):
        pass

class nurse(Staff):
    salary = "67,000"
    def getSalary(self):
        return self.salary
    def checkHealth(self, name):
        return f"{name} had their health checked."
    def tendTo(self, name):
        return f"{name} has been tended to."

class guidanceCounsler(Staff):
    salary = "60,000"
    def getSalary(self):
        return self.salary
    def counsel(self):
        return f"{name} has been counseled"

class secratary(Staff):
    salary = "55,000"
    def getSalary(self):
        return self.salary
    def greet(self):
        return f"Person greeted."
    def doClericalDuty(self):
        return f"Clerical duty done."

class cafetieriaWorker(Staff):
    salary = "30,000"
    def getSalary(self):
        return self.salary
    def serveFood(self):
        return f"Lunch is served."
    def cleanCafetieria(self):
        return f"Cafetieria is cleaned."
    def assistStudent(self, name):
        return f"{name} assisted."

# Creates the roles
def createStaffRoles(role, salary, hoursWorkedWeek, experienceYears):
    mapping = {
        "Teacher": teacher,
        "Principal": principal,
        "Vice Principal": vicePrincipal,
        "Custodian": custodian,
        "Resource Officer": resourceOfficer,
        "Coach": coach,
        "IT": it,
        "Nurse": nurse,
        "Guidance Counsler": guidanceCounsler,
        "Cafetieria Worker": cafetieriaWorker,
        "Secratary": secratary,
        "Librarian": librarian,
    }

    return mapping[role](role, salary, hoursWorkedWeek, experienceYears)
