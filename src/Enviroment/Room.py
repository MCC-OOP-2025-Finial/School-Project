"""Room implementations for the environment.

This module provides a concrete BaseRoom class and a few
specialized subclasses (Classroom, Laboratory). Use subclasses
when you want room-specific behavior (capacity, equipment, etc.).
"""

from typing import Any, Dict, List, Optional


class BaseRoom:
    """A general-purpose room.

    Attributes:
        name: human-readable name
        description: short description
        actors: list of actors currently in the room
        items: list of items in the room
        exits: mapping of direction -> other BaseRoom
    """

    def __init__(self, name: str, description: str, actors: Optional[List[Any]] = None):
        self.name: str = name
        self.description: str = description
        self.actors: List[Any] = actors or []
        self.items: List[Any] = []
        self.exits: Dict[str, "BaseRoom"] = {}

    def describe(self) -> str:
        parts: List[str] = [f"{self.name}: {self.description}"]
        if self.actors:
            parts.append("Actors: " + ", ".join(getattr(a, "name", str(a)) for a in self.actors))
        if self.items:
            parts.append("Items: " + ", ".join(str(i) for i in self.items))
        if self.exits:
            parts.append("Exits: " + ", ".join(self.exits.keys()))
        return "\n".join(parts)

    # Actor management
    def add_actor(self, actor: Any) -> None:
        if actor in self.actors:
            return
        self.actors.append(actor)

    def remove_actor(self, actor: Any) -> None:
        try:
            self.actors.remove(actor)
        except ValueError:
            raise ValueError("Actor not present in room")

    def list_actors(self) -> List[Any]:
        return list(self.actors)

    # Item management
    def add_item(self, item: Any) -> None:
        self.items.append(item)

    def remove_item(self, item: Any) -> None:
        try:
            self.items.remove(item)
        except ValueError:
            raise ValueError("Item not present in room")

    def list_items(self) -> List[Any]:
        return list(self.items)

    # Exits
    def connect_exit(self, direction: str, other: "BaseRoom") -> None:
        """Connect this room to another room in a given direction."""
        self.exits[direction] = other

    def get_exit(self, direction: str) -> Optional["BaseRoom"]:
        return self.exits.get(direction)


class Classroom(BaseRoom):
    """A classroom with a limited capacity."""

    def __init__(self, name: str, description: str, capacity: int, actors: Optional[List[Any]] = None):
        super().__init__(name, description, actors)
        self.capacity = int(capacity)

    def add_actor(self, actor: Any) -> None:
        if len(self.actors) >= self.capacity:
            raise ValueError("Classroom is full")
        super().add_actor(actor)


class Laboratory(BaseRoom):
    """A laboratory that tracks equipment and may restrict certain items."""

    def __init__(self, name: str, description: str, equipment: Optional[List[str]] = None, actors: Optional[List[Any]] = None):
        super().__init__(name, description, actors)
        self.equipment: List[str] = equipment or []

    def describe(self) -> str:
        base = super().describe()
        if self.equipment:
            base += "\nEquipment: " + ", ".join(self.equipment)
        return base


__all__ = ["BaseRoom", "Classroom", "Laboratory"]
import random
from typing import List, Any, Optional, Iterable 

class Room:
        
    def __init__(self, , actors: Optional[]): 
        self.name = name
        self.actors = actors

class classroom(Room):
    


        """
        self.items = []
        print(f"Room '{self.name}' created.")
        """

    


    #TODO - Implement Room class
    print("Room class is under construction")
    