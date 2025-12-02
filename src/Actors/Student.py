#Caleb
import random
from Actors.Actor_Main import ActorMain
from Data.Classes import Classes


class Student(ActorMain):
    """
    Represents a student in the system, inherits from ActorMain.
    """

    def __init__(self, major=None, gpa=None, schedule=None, **kwargs):
        # Initialize inherited attributes (name, id, etc.)
        super().__init__(**kwargs)

        # Student-specific attributes
        self.major = major or "Undeclared"
        self.gpa = gpa or 0.0

        # Student class schedule (list of class names)
        self.schedule = schedule or random.sample(Classes, k=4)
        self.current_class = None

    def next_period(self):
        """
        Moves the student to the next class in the schedule.
        Returns the class name for simulator use.
        """
        if not self.schedule:
            print(f"{self.name} has no more classes today.")
            self.current_class = None
            return None
        
        # Pop next class from schedule
        self.current_class = self.schedule.pop(0)
        print(f"{self.name} moves to {self.current_class}")
        return self.current_class

    def attend_class(self):
        """Simulates attending the current class."""
        if self.current_class:
            print(f"{self.name} is attending {self.current_class}.")
        else:
            print(f"{self.name} is not in a class right now.")

    def __str__(self):
        return f"Student {self.name} ({self.id}) - Major: {self.major}, GPA: {self.gpa} | Email: {self.email} | Current Class: {self.current_class or 'None'} | Schedule: {', '.join(self.schedule) if self.schedule else 'No more classes today.'} | Location: {self.location} "