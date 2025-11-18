from Actors.Actor_Main import ActorMain
import random
from Utility import DeniedRoleMethod

class Staff(ActorMain):
    def __init__(self, role, salary=0, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        # Allow passing actor fields like name, age, etc. via kwargs
        super().__init__(**kwargs)
        self.role = role
        self.salary = salary
        self.hoursWorkedWeek = hoursWorkedWeek
        self.experienceYears = experienceYears


    # Error handling
    

    def calculateSalary(self):
# Determines salary based on staff role.
        salaries = {
        "Teacher": 63000,
        "Principal": 104000,
        "Vice Principal": 86000,
        "Custodian": 30000,
        "Resource Officer": 79000,
        "Coach": 43000,
        "IT": 54000,
        "Nurse": 67000,
        "Guidance Counselor": 60000}

    def teach(self):
        if self.role != "Teacher" or "Coach":
            raise DeniedRoleMethod("This role can't use this method.")

    def prepareLesson(self):
        if self.role != "Teacher" or "Coach":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def recordAttendance(self) :
        if self.role != "Teacher" or "Coach":
            raise DeniedRoleMethod("This role can't use this method.")

    def sendAnnouncement(self):
        if self.role != "Principal" or "Vice Principal":
            raise DeniedRoleMethod("This role can't use this method.")
        
    def evaluateTeacher(self):
        if self.role != "Principal":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def cleanRoom(self):
        if self.role != "Custiodian":
            raise DeniedRoleMethod("This role can't use this method.")

    def resupplyRoom(self):
        if self.role != "Custodian":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def apprehend(self):
        if self.role != "Resource Officer":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def search(self):
        if self.role != "Resource Officer":
            raise DeniedRoleMethod("This role can't use this method.")

    def fixComputer(self):
        if self.role != "IT":
            raise DeniedRoleMethod("This role can't use this method.")

    def checkHealth(self):
        if self.role != "Nurse":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def tendTo(self):
        if self.role != "Nurse":
            raise DeniedRoleMethod("This role can't use this method.")

    def counsel(self):
        if self.role != "Guidance Counsler":
            raise DeniedRoleMethod("This role can't use this method.")

    def greet(self):
        if self.role != "Secratary":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def ClericalDuty(self):
        if self.role != "Secratary":
            raise DeniedRoleMethod("This role can't use this method.")

    def serveFood(self):
        if self.role != "Cafetieria Worker":
            raise DeniedRoleMethod("This role can't use this method.")

    def cleanCafetieria(self):
        if self.role != "Cafetieria Worker":
            raise DeneiedRoleMethod("This ")

class cafetieriaWorker(Staff):
    salary = "30,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Cafeteria Worker", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def serveFood(self):
        return f"Lunch is served."

    def cleanCafetieria(self):
        return f"Cafetieria is cleaned."

    def assistStudent(self, name):
        return f"{name} assisted."
    
class librarian(Staff):
    salary = "69,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Librarian", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def checkOutBook(self):
        return f"Book checked out."

