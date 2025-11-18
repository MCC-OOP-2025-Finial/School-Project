import random
import string

# Local fallback lists to generate random names
FIRST_NAMES = ["Alex", "Jordan", "Taylor", "Sam", "Chris", "Jamie", "Morgan", "Casey"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Davis", "Garcia", "Miller", "Wilson", "Anderson"]

def generate_random_name():
    """Generates a random full name without external libraries."""
    return random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES)

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
        self.name = name or generate_random_name()
        self.age = age or random.randint(18, 65)

        # Generate simple email
        last = self.name.split()[-1].lower()
        self.email = email or f"{last}{self.id.lower()}@school.edu"

        self.gender = gender or random.choice(["Male", "Female"])

        # Movement + schedule
        self.schedule = schedule or {}
        self.location = location or "Unknown"

        # Contacts
        self.phoneNumber = phoneNumber or "000-000-0000"
        self.emergencyContact = emergencyContact or "None"

    def Goto(self, location: str):
        """Move the actor to a different location."""
    def set_schedule(self, schedule_dict):
        self.schedule = schedule_dict
        
    def Goto(self, location):
        self.location = location
        return f"{self.name} is going to {location}."
