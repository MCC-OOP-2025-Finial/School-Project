#Elijah
from typing import List, Any, Optional  #Import type hints for List, Any, and Optional types
from Actors.Staff import Staff  # Import the Staff class from the Actors module

# Define the Room class to represent a room in the environment
class Room:
   

    def __init__(self, name: str, description: str, actors: Optional[List[Any]] = None, teacher: Optional[Staff] = None): 
        """Create a Room.

        Avoid using mutable default arguments. If callers supply lists they are used,
        otherwise new lists are created per-instance.
        """
        # Store the room's name/description
        self.name = name  
        self.description = description  

        # Create a copy of the actors list if provided, otherwise initialize empty list/ store teacher refrence
        self.actors = list(actors) if actors is not None else [] 
        self.teacher = teacher  

        # Print a message confirming the room has been created / add teacher to the actor list of a an empty room 
        print(f"Room '{self.name}' created.")  
        if self.teacher is not None:  
            self.add_actor(self.teacher)  

     # Define a method to add an actor to the room   
    def add_actor(self, actor: Any): 
        """
        Add an actor to the room.
        Args:
            actor (Any): The actor to add to the room.
        Returns:
            None
        """

        # Check if actor is not in room/ add actor to actor list/ print message of of actor entering 
        if actor not in self.actors: 
            self.actors.append(actor)  
            print(f"{actor.name} has entered {self.name}.")  

    # Define a method to remove an actor from the room     
    def remove_actor(self, actor: Any):  
        """
        Remove an actor from the room.
        Args:
            actor (Any): The actor to remove from the room.
        Returns:
            None
        """
        # Check if actor is in room/ remove actor from actor list/ print message of actor leaving
        if actor in self.actors:  
            self.actors.remove(actor)  
            print(f"{actor.name} has left {self.name}.")  
            
    # Define the string representation method for the Room class
    def __str__(self):  
        """Return a string description of the room, including its actors."""
        
        # Create a list with intial room description/ append room description to the lisrt 
        description = [f"You are in the **{self.name}**."]  
        description.append(self.description)  
        
        # Check if actors are currently in room/ creares a list of actor names (filtering only 'name' attribute)/Append message listing actors in room 
        if self.actors:  
            actor_names = [a.name for a in self.actors if hasattr(a, 'name')]  
            description.append(f"You see the following people here: {', '.join(actor_names)}.") 
             
        # Join all description lines with newlines and return as a single string
        return "\n".join(description)  