#Caleb/James/Elijah/Wilfried
import random
import string
import names # type: ignore

class ActorMain:
    """
    Base class for all school actors (students, teachers, staff).
    
    
    
    
    Attributes:
    
        id (str): Unique identifier for the actor.
        
        name (str): Full name of the actor.
        
        age (int): Age of the actor.
        
        email (str): Email address of the actor.
        
        gender (str): Gender of the actor.
        
        schedule (dict): Daily schedule of the actor.
        
        location (str): Current location of the actor.
        
        phoneNumber (str): Phone number of the actor.
        
        emergencyContact (str): Emergency contact information.
        
    Methods:

        Goto(location): Changes the actor location to the specified location.
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
    
    def Goto(self, location):
        """ 
            *  Goto method to change actor's location.
            *
            * Parameters:
            *   location (str): The new location to go to.
            *
            * Returns:
            *   str: Confirmation message of the new location.
        """
        self.location = location
        return f"{self.name} is going to {location}."