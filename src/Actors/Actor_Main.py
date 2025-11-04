import names
import random
import string

class ActorMain:
    """
    Base class for all actors in the system.
    """

    def __init__(self, 
                 name=None, 
                 age=None, 
                 email=None, 
                 gender=None, 
                 schedule=None, 
                 location=None, 
                 phoneNumber=None, 
                 emergencyContact=None):
        
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.name = name or names.get_full_name()
        self.age = age or random.randint(18, 65)
        self.email = email or (self.name.split()[1].lower() + "@example.com")
        self.gender = gender or random.choice(["Male", "Female"])
        self.schedule = schedule or {}
        self.location = location or "Unknown"
        self.phoneNumber = phoneNumber or "000-000-0000"
        self.emergencyContact = emergencyContact or "None"
        
    def Goto(self, location):
        self.location = location
        return f"{self.name} is going to {location}."
