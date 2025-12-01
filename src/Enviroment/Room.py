import random
from typing import List, Any, Optional 
from Actors.Staff import Staff

class Room:
    

    def __init__(self, name: str, description: str, actors: Optional[List[Any]] = None, teacher: Optional[Staff] = None): 
        """Create a Room.

        Avoid using mutable default arguments. If callers supply lists they are used,
        otherwise new lists are created per-instance.
        """
        self.name = name
        self.description = description


        self.actors = list(actors) if actors is not None else []
        # store the teacher (may be None)
        self.teacher = teacher

        print(f"Room '{self.name}' created.")
        # only add the teacher to the actors list if provided
        if self.teacher is not None:
            self.add_actor(self.teacher)
        
    def add_actor(self, actor: Any):

        if actor not in self.actors:
            self.actors.append(actor)
            print(f"{actor.name} has entered {self.name}.")
            
    def remove_actor(self, actor: Any):

        if actor in self.actors:
            self.actors.remove(actor)
            print(f"{actor.name} has left {self.name}.")
            
    
    def __str__(self):
        
        description = [f"You are in the **{self.name}**."]
        description.append(self.description)
        
        if self.actors:
            actor_names = [a.name for a in self.actors if hasattr(a, 'name')]
            description.append(f"You see the following people here: {', '.join(actor_names)}.")
            
        return "\n".join(description)