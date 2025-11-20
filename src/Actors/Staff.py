from Actors.Actor_Main import ActorMain
import random
from Utility import DeniedRoleMethod

# Staff interface
class Staff(ActorMain):
    def __init__(self, role, salary=0, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(**kwargs)
        self.role = role
        self.salary = salary
        self.hoursWorkedWeek = hoursWorkedWeek
        self.experienceYears = experienceYears

    # Determines salary based on staff role.
    def calculateSalary(self):
        salaries = {
        "Teacher": 63000,
        "Principal": 104000,
        "Vice Principal": 86000,
        "Custodian": 30000,
        "Resource Officer": 79000,
        "Coach": 43000,
        "IT": 54000,
        "Nurse": 67000,
        "Guidance Counselor": 60000,
        "Librarian": 30000}

    # All staff methods check role attribute of object before running
    # If the role attribute is not listed in the method, a custom error is raised

    # Teacher/Coach methods
    def startTeaching(self):
        if self.role != "Teacher" or "Coach":
            raise DeniedRoleMethod("This role can't use this method.")

    def stopTeaching(self):
        if self.role != "Teacher" or "Coach":
            raise DeniedRoleMethod("This role can't use this method.")

    def prepareLesson(self):
        if self.role != "Teacher" or "Coach":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def recordAttendance(self) :
        if self.role != "Teacher" or "Coach":
            raise DeniedRoleMethod("This role can't use this method.")

    # Principal/Vice Principal methods
    def sendAnnouncement(self):
        if self.role != "Principal" or "Vice Principal":
            raise DeniedRoleMethod("This role can't use this method.")
        
    def evaluateTeacher(self):
        if self.role != "Principal":
            raise DeniedRoleMethod("This role can't use this method.")

    # Custodian methods
    def cleanRoom(self):
        if self.role != "Custiodian":
            raise DeniedRoleMethod("This role can't use this method.")

    def resupplyRoom(self):
        if self.role != "Custodian":
            raise DeniedRoleMethod("This role can't use this method.")

    # Resource Officer methods
    def apprehend(self):
        if self.role != "Resource Officer":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def search(self):
        if self.role != "Resource Officer":
            raise DeniedRoleMethod("This role can't use this method.")

    # IT methods
    def fixComputer(self):
        if self.role != "IT":
            raise DeniedRoleMethod("This role can't use this method.")

    # Nurse methods
    def checkHealth(self):
        if self.role != "Nurse":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def tendTo(self):
        if self.role != "Nurse":
            raise DeniedRoleMethod("This role can't use this method.")

    # Guidance Counseler methods
    def counsel(self):
        if self.role != "Guidance Counsler":
            raise DeniedRoleMethod("This role can't use this method.")

    # Secratary methods
    def greet(self):
        if self.role != "Secratary":
            raise DeniedRoleMethod("This role can't use this method.")
    
    def ClericalDuty(self):
        if self.role != "Secratary":
            raise DeniedRoleMethod("This role can't use this method.")

    # Cafetieria Worker methods
    def serveFood(self):
        if self.role != "Cafetieria Worker":
            raise DeniedRoleMethod("This role can't use this method.")

    def cleanCafetieria(self):
        if self.role != "Cafetieria Worker":
            raise DeniedRoleMethod("This role can't use this method.")

    def assistStudent(self):
        if self.role != "Cafetieria Worker":
            raise DeniedRoleMethod("This role can't use this method.")

    # Librarian methods
    def checkOutBook(self):
        if self.role != "Librarian":
            raise DeniedRoleMethod("This role can't use this method.")

