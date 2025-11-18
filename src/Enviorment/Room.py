import Actor_Main as ActorMain # Retained original import, though not strictly needed here
import random
from typing import List, Any, Optional 

class Room:
    

    def __init__(self, name: str, description: str, actors: Optional[List[Any]] = None): 
        
        self.name = name
        self.description = description
        
        
        self.actors = actors if actors is not None else []
        self.items = []
        print(f"Room '{self.name}' created.")
        
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
    
