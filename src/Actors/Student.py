from Actor_Main import ActorMain

class Student(ActorMain):
    """
    Represents a student in the system, inherits from ActorMain.
    """
    def __init__(self, major=None, gpa=None, **kwargs):
        # Call the base class constructor to initialize common attributes
        super().__init__(**kwargs)
        
        # Add Student-specific attributes
        self.major = major or "Undeclared"
        self.gpa = gpa or 0.0
        
    def __str__(self):
        return f"Student {self.name} ({self.id}) - Major: {self.major}, GPA: {self.gpa}"
