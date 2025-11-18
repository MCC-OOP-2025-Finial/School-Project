from Actors.Actor_Main import ActorMain
import random


class Staff(ActorMain):
    """
    Represents a staff member in the school.
    Inherits from ActorMain and adds role, salary, and experience data.
    """

    def __init__(self, role: str, experienceYears: int = None, **kwargs):
        # Pass all inherited attributes (name, age, etc.)
        super().__init__(**kwargs)

        self.role = role
        self.experienceYears = (
            experienceYears if experienceYears is not None else random.randint(1, 35)
        )
        self.salary = self.calculateSalary()

    def calculateSalary(self):
        """Determines salary based on staff role."""
        salaries = {
            "Teacher": 63000,
            "Principal": 104000,
            "Vice Principal": 86000,
            "Custodian": 30000,
            "Resource Officer": 79000,
            "Coach": 43000,
            "IT": 54000,
            "Nurse": 67000,
            "Guidance Counselor": 60000
        }
        return salaries.get(self.role, 40000)

    def __str__(self):
        return (
            f"{self.role} {self.name} (ID: {self.id}) — "
            f"Experience: {self.experienceYears} yrs, Salary: ${self.salary:,}"
        )
