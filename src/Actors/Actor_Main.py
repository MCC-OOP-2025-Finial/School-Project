import random
import string
import names # type: ignore







class ActorMain:
    """
    Base class for all school actors (students, teachers, staff).
    """
    def __init__(
        self,
        name=None,
        age=None,
        email=None,
        gender=None,
        schedule=None,
        location=None,
        phoneNumber=None,
        emergencyContact=None
    ):
        
        # Unique actor ID
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        
        # Generate identity data
        self.gender = gender or random.choice(["Male", "Female"])
        self.name = name or names.get_full_name(gender=self.gender)
        self.age = age or random.randint(18, 65)

        # Generate simple email
        last = self.name.split()[-1].lower()
        self.email = email or f"{last}@school.edu"

        

        # Movement + schedule
        self.schedule = schedule or {}
        self.location = location or "Unknown"

        # Contacts
        self.phoneNumber = phoneNumber or "000-000-0000"
        self.emergencyContact = emergencyContact or "None"

   
    def set_schedule(self, schedule_dict):
        self.schedule = schedule_dict
        
    def Goto(self, location):
        self.location = location
        return f"{self.name} is going to {location}."