import Actor_Main as ActorMain
import random

class Staff(ActorMain.ActorMain):
    """
    Args:
        ActorMain (Type[ActorMain]): The base class for all actors in the system.
    """
        def __init__(self, role, salary, hoursWorkedWeek, experienceYears):
        super().__init__()
        self.role = role
        self.experienceYears = random.randint(0,35)
        self.salary = self.calculateSalary()
    
    def calcualteSalary(self)
        #Calculates salary based off staff role
        if self.role == "Teacher":
            return "63,000"
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
        elif self.role == "It":
            return "54,000"
        elif self.role = "Nurse":
            return "67,000"
        elif self.role = "Guidance Counsler":
            return "60,000"

    #TODO - Implement Staff class
    print("Staff class is under construction")
    