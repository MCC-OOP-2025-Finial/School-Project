from Actors.Actor_Main import ActorMain
import random
from Utility import DeniedRoleMethod

# Staff interface
class Staff(ActorMain):
    def __init__(self, role, salary=0, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(**kwargs)
        self.role = role
        self.salary = salary if salary != 0 else self.calculateSalary()
        self.hoursWorkedWeek = hoursWorkedWeek
        self.experienceYears = random.randint(0, 35)

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
        "Librarian": 30000,
        "Cafeteria Worker": 30000,
        "Secratary": 39000,
        }
        # Use dict.get to retrieve salary by role; calling the dict like a function
        # raises TypeError ('dict' object is not callable).
        return salaries.get(self.role, 0)

    # All staff methods check role attribute of object before running
    # If the role attribute is not listed in the method, a custom error is raised

    # Teacher/Coach methods
    def startTeaching(self):
        if self.role not in ("Teacher", "Coach"):
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is starting the lesson in this room: {self.location}."

    def stopTeaching(self):
        if self.role not in ("Teacher", "Coach"):
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is ending the lesson in this room: {self.location}."

    def prepareLesson(self):
        if self.role not in ("Teacher", "Coach"):
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is preparing the lesson materials."
    
    def recordAttendance(self) :
        if self.role not in ("Teacher", "Coach"):
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is recording attendance for their class."

    # Principal/Vice Principal methods
    def sendAnnouncement(self):
        if self.role not in ("Principal", "Vice Principal"):
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is sending an announcement to all staff and students."
        
    def conductAssembly(self):
        if self.role != "Principal":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is conducting an assembly in the Gymnasium or Auditorium."
        
    # Custodian methods
    def cleanRoom(self):
        if self.role != "Custodian":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is cleaning the room: {self.location}."

    def resupplyRoom(self):
        if self.role != "Custodian":
            raise DeniedRoleMethod("This role can't use this method.")
        """
        Further logic with the item inventory can be added here.
        """
        return f"{self.role} {self.name} is resupplying the room: {self.location}."

    # Resource Officer methods
    def apprehend(self):
        if self.role != "Resource Officer":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is apprehending a suspect on school grounds."
    
    def search(self):
        if self.role != "Resource Officer":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is conducting a search on school grounds."

    # IT methods
    def fixComputer(self):
        if self.role != "IT":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is fixing a computer issue."

    # Nurse methods
    def checkHealth(self):
        if self.role != "Nurse":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is checking a student's health."
    
    def tendTo(self):
        if self.role != "Nurse":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is tending to a student's injury."

    # Guidance Counselor methods
    def counsel(self):
        if self.role != "Guidance Counslor":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is counseling a student."

    # Secratary methods
    def greet(self):
        if self.role != "Secratary":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is greeting visitors at the front desk."
    
    def ClericalDuty(self):
        if self.role != "Secratary":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is performing clerical duties."

    # Cafeteria Worker methods
    def serveFood(self):
        if self.role != "Cafeteria Worker":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is serving food in the cafeteria."

    def cleanCafeteria(self):
        if self.role != "Cafeteria Worker":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is cleaning the cafeteria."

    def assistStudent(self):
        if self.role != "Cafeteria Worker":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is assisting a student in the cafeteria."

    # Librarian methods
    def checkOutBook(self):
        if self.role != "Librarian":
            raise DeniedRoleMethod("This role can't use this method.")
        return f"{self.role} {self.name} is checking out a book to a student."

